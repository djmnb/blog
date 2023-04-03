---
title: Docker总结
date: 2022/12/2
tags: docker
cover: /img/k8s-3assets/image-20221213104035867.png
---



## 什么是docker

Docker 使用 Google 公司推出的 Go 语言 进行开发实现，基于 Linux 内核的 cgroup，namespace，以及 OverlayFS 类的 Union FS 等技术，对进程进行封装隔离，属于操作系统层面的虚拟化技术(虚拟机是属于软件层面的虚拟化技术)。由于隔离的进程独立于宿主和其它的隔离的进程(既然是一个进程,当然能够直接使用系统资源)，因此也称其为容器

> 以下所有操作均在CentOS Linux release 7.6.1810 (Core)中进行,仅供参考哦,不同版本可能回有区别

## 为什么要用docker

传统的虚拟技术是利用软件虚拟出一套硬件环境,而且还需要再跑一个操作系统,所以无论执行速度,内存损耗,文件存储,都比传统的虚拟技术,而且一套dockerfile可以保证相同的环境,一次创建,到处可以运行,Docker 使用的分层存储以及镜像的技术，使得应用重复部分的复用更为容易，也使得应用的维护更新更加简单，基于基础镜像进一步扩展镜像也变得非常简单,因此docker有以下几个优势

* 更高效的利用系统资源
* 更快的启动速度
* 一致运行环境
* 更轻松的迁移
* 更轻松的拓展与维护

## 搭建与卸载

### 安装

```shell
# 下载包管理工具
yum install -y yum-utils 

#设置docker下载源为清华源
yum-config-manager \
    --add-repo \
    https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/centos/docker-ce.repo
# 安装docker   
yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

```

#### 启动docker服务

```shell
#启动docker 并且设置开机自启动
systemctl enable docker --now
```

#### 配置docker镜像加速源

```shell
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors":["https://o13jbvy6.mirror.aliyuncs.com"],
  "exec-opts": ["native.cgroupdriver=systemd"],
}
EOF
systemctl daemon-reload
systemctl restart docker
```

### 卸载

```shell
yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
# 查看还有哪些配置没删掉
whereis docker
# docker: /etc/docker /usr/libexec/docker
#删掉所有相关配置
rm -rf /etc/docker /usr/libexec/docker

```

## 镜像

Docker的镜像是一个特殊的文件系统,提供容器运行时所需要的程序,库,资源,配置,以及运行时准备的参数(环境变量,用户)等等,镜像不包含动态数据,构建好后,镜像的内容也不会发生改变

### 分层存储

docker的镜像是由基础镜像一层一层构建过来的,每一层的内容都只可读不可以更改,这么设计的好处是可以共享镜像,如果需要更改只能在容器层记录哪些文件被更改了,所有我们尽量把那些需要更改的文件通过容器卷的方式传递给容器,因为容器卷里面的东西不属于镜像,属于宿主机,

### registry

这个就代表镜像所在的仓库

### repository

这个是一组镜像的集合,比如centos镜像的所有版本,所以,repository是镜像的集合,registry是repository的集合

### manifest

主要存在与registry中作为docker镜像的元数据文件,在pull,push,save,load中作为镜像结构与基础信息的描述文件

## 容器

容器其实就是一个进程,但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 命名空间。因此容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全

容器启动时,在镜像的基础上加了一层**容器存储层**,所有的更改操作都进行在这一层,当容器死亡的时候,这一层也将消失

## 常用命令

### pull

拉取一个镜像

```shell
docker pull (地址/仓库/)镜像名字:版本号(没有版本号默认拉取最新版)
```

### images

查看所有镜像 

### rmi

删除一个镜像

```shell
docker rmi 镜像名字或者id
docker rmi $(docker images -q)  # 删除所有镜像
```

### run

基于镜像启动一个容器

* -i 开启交互式
* -t 分配一个终端
* -d 后台运行 
* -p 本地端口:容器端口 做端口映射
*  --privileged 在容器内真正的拥有root权限
* -v 设置容器卷
* -w 设置进入容器的工作目录
* --rm 容器退出后,删除容器
* --name 设置名字
* --network 设置要连接到网络名字
*  --entrypoint 设置容器启动时执行的命令,如果用了这个参数,后面输入的shell命令会当成参数

> 如果镜像不存在,会去自动拉取

### exec

进入一个运行中的容器

```shell
docker exec -it 容器名字/id bash(进入方式)
```

* -i 将当前终端输入流给容器
* -t 分配一个终端
* -w 指定工作目录
* -e 指定环境变量
* -u 指定用户

### logs

查看容器后台输出的信息,方便我们纠错

### stop

关闭一个容器  docker stop  id或者名字

### restart

重启一个容器 docker restart id 或者名字

### rm

删掉一个容器

```shell
docker rm -f id或者名字
docker rm -f $(docker ps -aq) #删除所有容器
```

### rename

更改容器的名字

### ps

与linux的ps功能差不多

* docker ps 查看运行的容器
* docker ps -a 查看运行和停止的容器

### commit

将容器打包成镜像(不推荐使用,建议使用build),这个

* --message 打包说明
* --author 作者
* docker commit 容器  (仓库名字)镜像:标签

### diff

拿容器层与镜像层做对比,看多了哪些,修改了哪些,删除了哪些东西

### inspect

查看容器,网络,镜像,容器卷,网络的详细信息或者说元信息

### network

* create -d 类型(一般用bridge,也是默认值) 网络名字 创建一个网络
* rm 删除一个网络
* prune 删除未使用的网络
* connect 将容器加入到某个网络当中去

### volume 

* create name 创建一个容器卷
* rm name/id 删除一个容器
* inspect name/id 查看容器卷的元信息
* prune 删除没有在使用的容器卷(只要有容器挂载,不管是运行的容器,还是停止的容器,都算在使用)

### build

基于dockerfile构建一个镜像

```shell
docker build -t 镜像名字:版本  .
```

* -t 指定镜像名字与版本
* -f 指定dockerfile路径(默认在上下文中)
* 后面这个点 **.** 是指上下文路径  build的时候,会将这个路径下的所有文件打包发给docker 服务端

### history

查看镜像的构建历史命令

* --no-trunc 查看完整命令(默认只能看到前几个字符)

### tag

可以改变一个镜像的仓库名字,镜像名字,版本号

```shell
docker tag nginx:latest mynginx:v1
```

### export

将一个容器导出成一个文件,但是这么打包出来的镜像,它只会包含一层了,所以不会保存所有的commit记录,比如说你的CMD命令,entrypoint的这些都不会保存,因此在打出的镜像执行的时候需要去重新输入CMD命令才能保证容器继续运行

> export 只能打包容器

格式:  docker export 容器名字或者id -o 打包的名字.tar

```
docker export nginx -o mynginx.tar
```



### import 

将本地或者远程文件导入成镜像

格式:  docker import  打包镜像名字 镜像名字:版本

```shell
docker import ./my-nginx.tar my-nginx:v2
```

这样的镜像直接是运行不了的,需要我们手动输入命令

```shell
docker run -d --name mynginx nginx /docker-entrypoint.sh "nginx" "-g" "daemon off;" 
```



## 容器卷

挂在容器卷的几种方式:

* 先创建 容器卷 docker volume create --name vol (会创建 /var/lib/docker/volumes/vol/_data 然后 将这个目录挂载到容器指定目录上去
* 直接使用不存在的容器卷名字,docker会给我们创建一个容器卷假设名字为a,那么对应的目录就为 /var/lib/docker/volumes/a/_data
* 使用自定义文件或者文件夹,**必须使用绝对路径**,然后使用-v 宿主机路径:容器路径   如果两个路径都不存在,docker会为我们创建,如果容器路径存在,那么里面东西会被宿主机的东西覆盖

一个容器可以挂载多个容器卷,我们可以设置容器对容器卷的操作权限,比如只读 -v 宿主机路径:容器路径:ro

权限问题,当我们使用容器卷的时候,会发现里面的数据我们居然没办法查看,也没有办法创建文件,这个时候,我们需要使用  --privileged=true 创建容器

## 构建镜像

### commit

当我们使用commit 之后,是将当前容器的存储层+原来的镜像打包成一个新的镜像,这样容器的存储层就会被保留下来,后面也无法再更改,如果我们使用了卷的话,这个东西并不属于存储层,自然不会被保存

启动一个nginx的容器,并且修改它的index页面,然后commit打包成一个镜像

```shell
# 启动一个容器,并设置端口映射
docker run -d --name nginx -p 8080:80 nginx
# 进入这个容器
docker exec -it nginx bash
# 修改默认页面
echo "<h1>hello world</h1>" > /usr/share/nginx/html/index.html
# 退出容器 exit
# 访问虚拟机8080 端口 
curl localhost:8080 
# 输出<h1>hello world</h1>
# 将容器做成镜像
docker commit --author "djm" --message "修改了默认网页" nginx mynginx:v1 

docker images #查看我们自己的镜像
# 通过打包好的镜像启动容器
docker run -d --name nginx1  -p 8081:80 mynginx:v1
# 访问ip:8081就能访问到我们修改的页面

#不要使用docker commit 来制作镜像,这样会导致很多文件被加入到这一层中,到时候docker commit的次数越来越多,镜像会变得很臃肿
# 而且docker commit 制作镜像,别人根本不知道我们在基础镜像上面干了些什么东西
```

### dockerfile

```shell
# dockerfile 的编写

ARG 设置环境变量(放在FROM前面,变量只能在所有FROM里面使用,放在其他指令前面,只有那一个指令能用)
FROM 基础镜像(名字:版本号)  (scratch 空镜像)
ENV 设置环境变量(到时候容器里面会存在这个变量哦)
RUN 命令   
CP 源路径(相对于上下文来说) 目标路径(可以相对于容器来说,也可以相对于容器里面的工作目录(通过WORKDIR指定来说)
ADD 压缩包路径(相对于上下文) 目录路径(同上)  add 可以做其他的事(和cp一样的功能,下载文件),但是推荐只做这个事情
CMD ["可执行文件","参数"] 容器启动时默认执行命令,当然我们自己写的命令会替换掉这个,CMD里面的命令会最终被替换成
sh -c "可执行文件","参数"
ENTRYPOINT ["可执行文件","参数",CMD] 这个命令和CMD命令的目的都是一样的,让容器启动的时候执行一些命令,但是如果这个命令与CMD
一起使用的时候,CMD里面的东西会被当成参数,默认这个命令是不会被替换掉的,我们需要使用--entrypoint来指定
VOLUME 定义一个匿名卷,如果用户没有指定容器卷,我们也能挂在一个匿名卷,把动态数据放在容器卷中,这样就能防止一些动态数据的写操作发生在容器层
WORKDIR 指定容器的工作目录,可以使用绝对路径和相对路径,相对路径是相对于上次的WORKDIR来说的,最初始的WORKDIR在/ (这个是会影响到后面的层的)
USER 切换用户 ,这个用户必须事先存在(这个也会影响到后面的层
HEALTHCHECK 健康检查,检查容器有没有出什么异常,通过返回值判断
	HEALTHCHECK --interval=5s --timeout=3s CMD curl -fs http://localhost/ || exit 1  
	每5秒执行一次,如果超过这个时间没有返回数据,则说明出异常,返回0代表正常,1代表异常
ONBUILD 为子镜像执行的命令,后面可以跟RUN,CMD这些
```

```
dockerfile 的流程解释

要想明白dockerfile 咱们就得知道docker commit 制作镜像,dockerfile 其实也就是使用了它做镜像

FROM -> 启动一个容器
ENV -> 定义一些变量供下面的命令使用
RUN  -> 进入容器更改文件或者安装东西然后 commit  所以我们不要写很多run(如果有很多命令,我们可以使用&&连接起来) 
不然就会commit很多次,这样的镜像很臃肿 
(我们最好写一组清理工作的命令,将那些没有用的文件给删掉)
CP -> 将上下文里面的东西复制到容器里面 会将源文件的各种元数据都保留(所有者,所属组) 我们可以通过 --chown=user:group来更改
ADD -> 将压缩包解压,也可以使用--chown=user:group 这个参数
CMD -> 相当于 docker run -d CMD 这样,所有我们不要瞎写CMD,如果CMD命令执行完了,那么这个进程就执行完了,容器一起来就结束(cmd与ENTRYPOINT只会执行一次,多写了没用)
```

再以上面commit的例子来一遍dockerfile的操作

```shell

mkdir mynginx && cd mynginx

#默认支持dockerfile Dockerfile 可以构建的时候使用-f指定dockerfile的路径
vim Dockerfile
#编写dockerfile
FROM nginx
RUN echo "<h1>hello world DJM NB</h1>" > /usr/share/nginx/html/index.html

# 构建dockerfile 
docker build -t mynginx:v2 .  #这个.是上下文路径,不是dockerfile的路径哦

#输出的东西
Sending build context to Docker daemon 2.048 kB #将上下文的东西发给docker守护进程
Step 1/2 : FROM nginx
 ---> 88736fe82739
Step 2/2 : RUN echo "<h1>hello world DJM NB</h1>" > /usr/share/nginx/html/index.html
 ---> Running in fbccf519f6af

 ---> 873049df2a75
Removing intermediate container fbccf519f6af

#查看我们的镜像
docker images

#运行容器
docker run -d --name nginx2 -p 8082:80 mynginx:v2

#查看网页
```

docker build 的流程

首先将上下文中不在.dockerignore里面的文件全部(是全部哦,所以你的上下文中,不要多一些乱七八糟没有用的东西)发送给docker服务端(守护进程),然后再依次执行dockerfile里面的指令

注意点:   

* 默认情况下,是在上下文里面找dockerfile,不过我们可以通过-f 来指定dockerfile的路径
*  在dockerfile的编写时,使用cp 或者 add命令的时候, 要访问上下文里面的文件时候,要使用./ 开头,不能使用绝对路径这样,除非你把上下文放到了根目录下面,这样你会将硬盘里面的文件全部发送给守护进程



挖个坑

```dockerfile
# dockerfile
FROM centos:7
VOLUME /data
RUN touch /data/file

# 请问我将上面这个dockerfile build生成镜像然后运行容器的时候,这个文件会存在吗?

# 答案是:不会
我们来分析一下流程:
首先拿到基础镜像,启动一个挂在了本地无名容器卷的容器,这样容器里面就有了/data目录,然后在/data里面创建文件,然后进行提交
但是/data目录的东西并不会被打包,它不属于容器,提交后,docker再把这个无名卷删掉了,所有压根就不会有这个文件存在,只会有/data目录
总结: 要判断创建文件会不会存在镜像中,我们只需要判断这个文件的创建是在挂在容器卷之前还是之后,如果是挂在容器卷之前,而且正好是在容器卷下面创建的,那么不会存在,不然就会存在
这个VOLUME 选项就是为了防止用户不设置容器卷,也能有一个匿名卷,还有就是能给给使用者留点讯息
```



```shell
docker rm -f `docker ps -aq` 快速删除所有容器  docker ps -aq 是列出所用容器id 
```



* 


 **容器是否会长久运行，是和 `docker run` 指定的命令有关，和 `-d` 参数无关**

如果使用attach进入容器,退出后则会结束容器,但是使用exec命令



## docker-compose

这个东西是用来管理docker容器的,那么多docker容器,难道我们每次部署都要去一一启动并且配置吗?那多麻烦,得用docker-compose去管理

###  安装

```shell
curl -L https://get.daocloud.io/docker/compose/releases/download/v2.4.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
#赋予权限
chmod o+x /usr/local/bin/docker-compose
```

配置好自动自动补全

```shell
$ curl -L https://raw.githubusercontent.com/docker/compose/1.27.4/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose
```

### 卸载

```shell
rm -f /usr/local/bin/docker-compose
```

### 常用命令

​	我们使用docker-compose的时候可以指定一些参数

* -f 指定docker-compse.yml的位置(默认就在当前目录) 
* -p 指定项目名字(默认就是目录名字)

> docker-compose只有在具有docker-compose.yml目录下使用才有用(**除非指定docker-compse.yml的位置**),否则会提示
> no configuration file provided: not found

#### build

构建项目中的镜像,就是构建在配置文件中使用了build配置项的服务,如果有的话,则会构建一个镜像到仓库中,默认名字是当前目录名字+service对应的名字

#### config

检查配置文件是否正确,正确则显示完整配置文件,否则说明错误原因

#### down

删掉项目中通过up启动的服务,并且删除网络

#### exec

进入项目中的容器

#### images

列出compose文件中启动的容器对应的镜像

#### kill

杀掉一个项目中的服务(得使用服务名字哦)

#### stop

停止一个服务

#### up

这个命令巨屌好吧,帮我们省了不少事,它将尝试自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作

#### scale

指定开启服务个数,如果服务多于这个就停止,少了就增加 

### docker-compose.yml 模板

#### build

如果镜像存在则不会构建镜像,否则根据指定文件夹路径(可以是相对docker-compose.yml的路径,也可以是绝对路径)构建镜像,构建镜像的名字为当前docker-compose 文件所在目录的目录名+服务名字版本为最新版本,子命令

* context 指定dockerfile的位置

#### command

覆盖容器启动的时候执行的命令,也就是相当于在dockerfile后面多加一条CMD

#### devices

设备映射关系

```yml
devices:
  - "/dev/ttyUSB1:/dev/ttyUSB0"
```

#### depends_on

解决容器依赖关系,比如先得启动哪些服务,在启动自己

```yml

services:
  web:
    build: .
    depends_on:
      - db
      - redis
```

比如这个先启动,db,redis 然后就启动自己(不是等db,redis,完全启动后再启动自己哦)

#### dns

指定DNS服务器,可以是单个数据,也可以是列表

#### environment

指定环境变量

设置环境变量。你可以使用数组或字典两种格式。

只给定名称的变量会自动获取运行 Compose 主机上对应变量的值，可以用来防止泄露不必要的数据。

```yaml
environment:
  RACK_ENV: development
  SESSION_SECRET:


environment:
 - RACK_ENV=development
 - SESSION_SECRET
```

如果变量名称或者值中用到 `true|false，yes|no` 等表达 [布尔](https://yaml.org/type/bool.html) 含义的词汇，最好放到引号里，避免 YAML 自动解析某些内容为对应的布尔语义。

#### expose

暴露端口,但是不映射,互联在一个网络中的容器可以访问

```yaml
expose:
 - "3000"
 - "8000"
```

#### extra_hosts

```yaml
extra_hosts:
 - "mysql:123.323.12.12"
```

这个时候/etc/hosts下面会多

```
123.323.12.12 mysql
```

#### healthcheck

通过命令检查容器是否健康运行。

```yaml
healthcheck:

  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 1m30s
  timeout: 10s
  retries: 3
```

#### image

指定为镜像名称或镜像 ID。如果镜像在本地不存在，Compose 将会尝试拉取这个镜像,用这个镜像启动作为容器

#### logging

配置日志

#### port 

与docker run -p 里面的作用是差不多的

## 额外补充

### 打标签

如果我们虚拟机没有连接外网,但是我们本机可以连接外网,我们可以使用本地下载好后,上传到虚拟机,然后

## 遇到的坑

* 开启或者关闭防火墙后,一定要重启docker,不然会报错
* 如果挂载好容器卷发现在容器里面无法访问数据,权限出问题,那大概率是selinux没有设置成disabled   修改/etc/selinux/config 里面的SELINUX为disabled

* **Failed to get D-Bus connection: Operation not permitted** ,Docker的设计理念是在容器里面不运行后台服务，容器本身就是宿主机上的一个独立的主进程，也可以间接的理解为就是容器里运行服务的应用进程。一个容器的生命周期是围绕这个主进程存在的，所以正确的使用容器方法是将里面的服务运行在前台。但是要在容器里面运行一个服务也不是不可以,创建容器的时候使用 /usr/sbin/init作为启动执行命令,然后加入--privileged=true

  ```shell
  docker run -id -p 8081:22 --name centos7 --privileged=true  centos:7 /usr/sbin/init
  ```

  
