---
title: yolo框架学习
date: 2024-11-29
---

> 本文看的是yolov5的源代码, 后续的yolo除了网络架构不同, 其他地方是差不多的



# 数据集yaml编写规则

yolo的数据集加载类是LoadImagesAndLabels, 他搜索数据的方式如下:

1. 从所给目录拿到这个目录及其子目录下的所有文件

2. 然后进行筛选, 只保留图片文件

3. 根据图片文件搜索图片对应的标签文件, 方式很简单 **替换图片路径中最后一个 images 为 lables**

   代码如下:

   ```python
    sa, sb = f"{os.sep}images{os.sep}", f"{os.sep}labels{os.sep}"  # /images/, /labels/ substrings
    return [sb.join(x.rsplit(sa, 1)).rsplit(".", 1)[0] + ".txt" for x in img_paths]
   ```

根据这个规则, 我们其实就很容易搞懂怎么存放标签和图片, 只要标签和图片路径最后一个images和labels不同就行

比如: /images/a/b/c 和 /labels/a/b/c 可以, /a/b/c/images 和 /a/b/c/images 也可以, 这样就满足了大家喜欢的两种布局, 真的很巧妙



# 模型构建

根据模型yaml文件动态搭建,  源码如下:

```python
def parse_model(d, ch):
    """Parses a YOLOv5 model from a dict `d`, configuring layers based on input channels `ch` and model architecture."""
    LOGGER.info(f"\n{'':>3}{'from':>18}{'n':>3}{'params':>10}  {'module':<40}{'arguments':<30}")
    anchors, nc, gd, gw, act, ch_mul = (
        d["anchors"],
        d["nc"],
        d["depth_multiple"],
        d["width_multiple"],
        d.get("activation"),
        d.get("channel_multiple"),
    )
    if act:
        Conv.default_act = eval(act)  # redefine default activation, i.e. Conv.default_act = nn.SiLU()
        LOGGER.info(f"{colorstr('activation:')} {act}")  # print
    if not ch_mul:
        ch_mul = 8
    na = (len(anchors[0]) // 2) if isinstance(anchors, list) else anchors  # number of anchors
    no = na * (nc + 5)  # number of outputs = anchors * (classes + 5)

    layers, save, c2 = [], [], ch[-1]  # layers, savelist, ch out
    for i, (f, n, m, args) in enumerate(d["backbone"] + d["head"]):  # from, number, module, args
        m = eval(m) if isinstance(m, str) else m  # eval strings
        for j, a in enumerate(args):
            with contextlib.suppress(NameError):
                args[j] = eval(a) if isinstance(a, str) else a  # eval strings

        n = n_ = max(round(n * gd), 1) if n > 1 else n  # depth gain
        if m in {
            Conv,
            GhostConv,
            Bottleneck,
            GhostBottleneck,
            SPP,
            SPPF,
            DWConv,
            MixConv2d,
            Focus,
            CrossConv,
            BottleneckCSP,
            C3,
            C3TR,
            C3SPP,
            C3Ghost,
            nn.ConvTranspose2d,
            DWConvTranspose2d,
            C3x,
        }:
            c1, c2 = ch[f], args[0]
            if c2 != no:  # if not output, 保证输出通道数是ch_mul的倍数
                c2 = make_divisible(c2 * gw, ch_mul)

            args = [c1, c2, *args[1:]]
            if m in {BottleneckCSP, C3, C3TR, C3Ghost, C3x}:
                args.insert(2, n)  # number of repeats
                n = 1
        elif m is nn.BatchNorm2d:
            args = [ch[f]]
        elif m is Concat:
            c2 = sum(ch[x] for x in f)
        # TODO: channel, gw, gd
        elif m in {Detect, Segment}:
            args.append([ch[x] for x in f])
            if isinstance(args[1], int):  # number of anchors
                args[1] = [list(range(args[1] * 2))] * len(f)
            if m is Segment:
                args[3] = make_divisible(args[3] * gw, ch_mul)
        elif m is Contract:
            c2 = ch[f] * args[0] ** 2
        elif m is Expand:
            c2 = ch[f] // args[0] ** 2
        else:
            c2 = ch[f]

        m_ = nn.Sequential(*(m(*args) for _ in range(n))) if n > 1 else m(*args)  # module
        t = str(m)[8:-2].replace("__main__.", "")  # module type
        np = sum(x.numel() for x in m_.parameters())  # number params
        m_.i, m_.f, m_.type, m_.np = i, f, t, np  # attach index, 'from' index, type, number params
        LOGGER.info(f"{i:>3}{str(f):>18}{n_:>3}{np:10.0f}  {t:<40}{str(args):<30}")  # print
        save.extend(x % i for x in ([f] if isinstance(f, int) else f) if x != -1)  # append to savelist
        layers.append(m_)
        if i == 0:
            ch = []
        ch.append(c2)
    return nn.Sequential(*layers), sorted(save)
```

这个东西确实好, 比起我们用代码构建模型方便太多了

在模型训练过程中, 会记录每一层输出的东西, 如果某一层的来源有多个个, 就需要在上一层的时候就使用concat进行连接, 前向传播源码如下

```python
def _forward_once(self, x, profile=False, visualize=False):
        """Performs a forward pass on the YOLOv5 model, enabling profiling and feature visualization options."""
        y, dt = [], []  # outputs
        for m in self.model:
            if m.f != -1:  # if not from previous layer
                x = y[m.f] if isinstance(m.f, int) else [x if j == -1 else y[j] for j in m.f]  # from earlier layers, 如果有多层就使用多层数据, 这样下面的时候就必须使用concat, m就必须是concat, 或者在这里就concat
            if profile:
                self._profile_one_layer(m, x, dt)
            x = m(x)  # run
            y.append(x if m.i in self.save else None)  # save output
            if visualize:
                feature_visualization(x, m.type, m.i, save_dir=visualize)
        return x
```



# 缓存

yolo提供了 cache这个选项, 有三种: 

1. ram 在dataset里面一次将图片全部加载到内存中, 这种在使用的时候是最快的
2. disk 会在图片路径下创建同名的.npy文件, 需要的时候就是加载这个文件了, 这个文件是经过了处理图片后的numpy数组格式, 加载的时候更快
3. 不使用--cache, 每次使用图片的时候都从磁盘加载图片

有时候我们有疑惑, 为什么训练的时候三种速度一样?

**因为图片加载速度高于GPU训练速度**, 这个就要归功于pytorch的DataLoader了, 他会启用多个工作进程, 在GPU训练的时候,每个进程加载2*batch_size(可以自己设置)个数据到缓存队列中, 如果数据不大, 加载速度就可能快于GPU训练速度, 所以需要用的时候数据已经在内存了, 这样的话, 三个就没有区别

# 衡量标准计算

模型的好坏一般有些评判标准, 精度, 召回率, f1分数, AP, mAP(50, 50-95)

AP 是指 一个类别的平均精度, 是通过在一个Iou阈值下, 不同置信度产生的精度和召回率曲线与坐标轴围成的面积

mAP 就是指所有类别的平均了, mAP50 指 Iou为0.5的情况下, mAP的值,  mAP50-95 是指Iou 从0.5-0.95的mAP的平均值

Iou越大, 说明对于检测越加严格, 同样置信度越大, 也越严格