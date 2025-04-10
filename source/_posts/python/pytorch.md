---
title: pytorch学习
date: 2024-11-1
---



# nn模块



## 权重初始化

```python
import torch
import torch.nn as nn


# 定义线性层
linear_layer = nn.Linear(in_features=10, out_features=5)
# 直接赋值给权重和偏置
linear_layer.weight.data.fill_(0.01)  # 将权重全设置为 0.01
linear_layer.bias.data.fill_(0)       # 将偏置设置为 0
```



# 广播机制

广播机制的核心流程可以概括为：

1. **从右往左逐个对比两个张量的维度**。
2. **相等时继续**：如果对应维度大小相等，直接匹配。
3. **不相等时判断是否有1**：如果不相等，检查其中一个维度是否为1。如果是，则可以广播扩展成相等的维度。
4. **无法匹配时停止**：如果对应维度大小不相等，且都不为1，则广播机制无法继续，运算会报错。
5. **缺少的维度补1**：如果一个张量维度数量少，从右侧开始自动补充1，以便进行对比。

例如，如果有两个张量：

- `a` 的形状是 `(3, 1, 5)`
- `b` 的形状是 `(4, 5)`

按照广播机制，从右往左依次匹配：

- 最右边的维度 5 匹配。
- 中间的维度 `1`（`a` 的第二维）可以扩展到 4，以匹配 `b` 的第二维。
- `a` 的第一个维度 `3` 与 `b` 无需匹配，因为 `b` 没有对应的维度，所以直接保留。

最终 `a` 会广播为 `(3, 4, 5)`，`b` 会广播为 `(1, 4, 5)`，最后结果为 `(3, 4, 5)`。

> pytorch并不会真正的扩展原始数据维度, 而是在计算的时候重复利用原始数据

**注意**: 矩阵乘法(点积) 有自己的运算规则, 并不满足这种广播机制

# 技巧

## 损失函数数值图

我们在训练模型的时候, 推荐把每一轮的损失值画出来, 因为深度学习是个黑盒子, 我们很难得知他到底学啥了, 学的咋样了, 我们只有通过我们自己的评判标准也就是损失去判断, 所以把图画出来是最直观的, 也方便调试bug



# 问题

## 梯度爆炸

在使用MSELoss的时候, 如果reduction改成sum,  那么损失值跟batch就线性相关了, 很容易导致梯度爆炸,  就需要对这个reduction做调整, 要么使用mean, 要么自己去定义



# 显存分配

pytorch中, 显存分配有点类似于操作系统的内存分配, 都是按一个指定大小分配的, 我们可以通过下面几个函数来查看详情

1. torch.cuda.memory_allocated()  用于查看真实分配给我们程序使用的显存大小
2. torch.cuda.memory_reserved() 用于查看pytorch向GPU请求的显存大小
3. torch.cuda.memory_summary() 用于查看显存分配详情
4. torch.cuda.empty_cache() 用于归还多余的显存, 就是上述 第二个中, 没有被占用的块

## 分配块大小

```python
x = torch.zeros(1, requires_grad=True).cuda()

print(x.dtype)

allocate = torch.cuda.memory_allocated()
print(allocate) # 512B

cache = torch.cuda.memory_reserved()
print(cache) # 2097152/1024/1024 = 2MB
```

通过此种方式我们就发现pytorch向GPU申请的单位块为2MB,  pytroch分配给程序的最小块为512B(不同的pytorch版本可能这个数值不一样)

## memory_summary详情

```shell
|===========================================================================|
|                  PyTorch CUDA memory summary, device ID 0                 |
|---------------------------------------------------------------------------|
|            CUDA OOMs: 0            |        cudaMalloc retries: 0         |
|===========================================================================|
|        Metric         | Cur Usage  | Peak Usage | Tot Alloc  | Tot Freed  |
|---------------------------------------------------------------------------|
| Allocated memory      |     512 B  |     512 B  |     512 B  |       0 B  |  # pytorch分配给程序块的大小
|       from large pool |       0 B  |       0 B  |       0 B  |       0 B  |
|       from small pool |     512 B  |     512 B  |     512 B  |       0 B  |
|---------------------------------------------------------------------------|
| Active memory         |     512 B  |     512 B  |     512 B  |       0 B  |  # 
|       from large pool |       0 B  |       0 B  |       0 B  |       0 B  |
|       from small pool |     512 B  |     512 B  |     512 B  |       0 B  |
|---------------------------------------------------------------------------|
| GPU reserved memory   |    2048 KB |    2048 KB |    2048 KB |       0 B  |  # 向GPU申请的显存大小
|       from large pool |       0 KB |       0 KB |       0 KB |       0 B  |
|       from small pool |    2048 KB |    2048 KB |    2048 KB |       0 B  |
|---------------------------------------------------------------------------|
| Non-releasable memory |    2047 KB |    2047 KB |    2047 KB |       0 B  |  # 未归还给GPU显存的大小
|       from large pool |       0 KB |       0 KB |       0 KB |       0 B  |
|       from small pool |    2047 KB |    2047 KB |    2047 KB |       0 B  |
|---------------------------------------------------------------------------|
| Allocations           |       1    |       1    |       1    |       0    | #  分配次数
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       1    |       1    |       1    |       0    |
|---------------------------------------------------------------------------|
| Active allocs         |       1    |       1    |       1    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       1    |       1    |       1    |       0    |
|---------------------------------------------------------------------------|
| GPU reserved segments |       1    |       1    |       1    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       1    |       1    |       1    |       0    |
|---------------------------------------------------------------------------|
| Non-releasable allocs |       1    |       1    |       1    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       1    |       1    |       1    |       0    |
|---------------------------------------------------------------------------|
| Oversize allocations  |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Oversize GPU segments |       0    |       0    |       0    |       0    |
|===========================================================================|
```



## 显存占用成分

不变成分 + 可变成分

不变成分 = (模型参数 + 梯度参数 = 2 * 模型参数) + 优化器参数(2*模型参数, 一阶动量和二阶动量)

可变成分= 输入数据 + 中间层输出(最大输出) + 损失+模型输出

> 要牢记分配单位哦, 即使是一个字节也是分配一个块

## 代码展示

```python
import torch

temp = 0

def print_memory():
    global temp
    t = torch.cuda.memory_allocated()
    print(t - temp)
    temp = t

# 模型初始化
linear1 = torch.nn.Linear(1024,1024, bias=False).cuda() # + 4194304
print_memory()
linear2 = torch.nn.Linear(1024, 1024, bias=False).cuda() # + 4194304
print_memory()

linear3 = torch.nn.Linear(1024, 1, bias=False).cuda() # + 4096
print_memory()

# 输入定义
inputs = torch.tensor([[1.0]*1024]*1024).cuda() # shape = (1024,1024) # + 4194304
print_memory()

# 前向传播
x = linear1(inputs) # shape = (1024,1024) # memory + 4194304 
print_memory()
x = linear2(x) # shape = (1024,1) # memory + 4194304
print_memory()

x = linear3(x) # shape = (1) # memory + 4096
print_memory()


loss = sum(x) # shape = (1) # memory  + 512(loss虽然只有一个元素, 但是torch的最小分配是512)
print_memory()

# 后向传播
loss.backward() # memory + 4096 (这里的4096是最后一层的输出, 也就是上面的x的大小, 中间层的输出正好和梯度相互抵消, 但是最后一层的抵消不了, 需要保留这个输出)
print_memory()

loss = sum(linear3(linear2(linear1(inputs)))) # shape = (1) # memory + 4194304 + 4194304 (最后一层不需要再加了, 因为保留了, 512也没了，因为loss也还在)
print_memory()
loss.backward() #  - 4194304 - 4194304 = 4194304 + 4194304 + 4096 - 4194304 - 4194304 - 4096 - 4194304 - 4194304 
print_memory()

loss = sum(linear3(linear2(linear1(inputs)))) # shape = (1) # memory + 4194304 + 4194304 (最后一层不需要再加了, 因为保留了, 512也没了，因为loss也还在)
print_memory()
loss.backward() #  - 4194304 - 4194304 = 4194304 + 4194304 + 4096 - 4194304 - 4194304 - 4096 - 4194304 - 4194304 
print_memory()
```

总结: 如果输入数据大小不变, 那么第二次梯度更新之前,也就是第二次前向传播完成后 显存占用就会来到最大值, 后续都不会超过这个最大值,  因为第二次的时候, 保留了第一次的梯度, 第二次的中间输出, 而第一次是只保存了中间输出, 在梯度更新后就只保留了梯度

## 问题分析

这是我在一次验证结果的时候产生的现象, 也导致我来分析pytorch显存是怎么分配的:

验证过程中, 我的数据大小是从小到大再到小, 按理来说显存占用也应该是从小到大再到小, 可是实际上, 我的显存只升不降

导致此问题的正是pytorch的这种显存管理方式, 他从GPU申请的所有显存, 如果我们不主动使用empty_cache去释放多余显存, 他就会一直占用即使没有使用

**如果站在保证程序能够正常运行的角度来看, 也确实没必要归还, 因为我后续可能还需要这些显存, 如果不够了, 那就会出现问题, 导致程序跑失败**

