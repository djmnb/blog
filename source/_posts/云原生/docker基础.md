---
mvtitle: Docker总结
date: 2022/12/2
tags: docker
cover: /img/k8s-3assets/image-20221213104035867.png
---



# 什么是docker

Docker 使用 Google 公司推出的 Go 语言 进行开发实现，基于 Linux 内核的 cgroup，namespace，以及 OverlayFS 类的 Union FS 等技术，对进程进行封装隔离，属于操作系统层面的虚拟化技术(虚拟机是属于软件层面的虚拟化技术)。由于隔离的进程独立于宿主和其它的隔离的进程(既然是一个进程,当然能够直接使用系统资源)，因此也称其为容器

> 以下所有操作均在CentOS Linux release 7.6.1810 (Core)中进行,仅供参考哦,不同版本可能会有区别

# 为什么要用docker

传统的虚拟技术是利用软件虚拟出一套硬件环境,而且还需要再跑一个操作系统,所以无论执行速度,内存损耗,文件存储,都比传统的虚拟技术,而且一套dockerfile可以保证相同的环境,一次创建,到处可以运行,Docker 使用的分层存储以及镜像的技术，使得应用重复部分的复用更为容易，也使得应用的维护更新更加简单，基于基础镜像进一步扩展镜像也变得非常简单,因此docker有以下几个优势

* 更高效的利用系统资源
* 更快的启动速度
* 一致运行环境
* 更轻松的迁移
* 更轻松的拓展与维护

# 搭建与卸载

## 安装

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

### 启动docker服务

```shell
#启动docker 并且设置开机自启动
systemctl enable docker --now
```

### 配置docker镜像加速源

```shell
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors":["https://o13jbvy6.mirror.aliyuncs.com","https://docker.mirrors.ustc.edu.cn/"],
  "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF
systemctl daemon-reload
systemctl restart docker
```

```
https://docker.mirrors.ustc.edu.cn/
```



## 卸载

要在 Linux 系统上彻底卸载 Docker，请按照以下步骤操作：

1. 停止 Docker 服务：
```shell
sudo systemctl stop docker.service
```

2. 禁用 Docker 服务：
```shell
sudo systemctl disable docker.service
```

3. 删除 Docker 包。根据您的系统和安装方式，命令可能略有不同。

对于基于 Debian/Ubuntu 的系统，使用以下命令：
```
sudo apt-get purge docker-ce docker-ce-cli containerd.io
```

对于基于 RHEL/CentOS/Fedora 的系统，使用以下命令：
```
sudo yum remove docker-ce docker-ce-cli containerd.io
```
或者：
```
sudo dnf remove docker-ce docker-ce-cli containerd.io
```

4. 删除 Docker 相关的目录和文件。以下命令将删除 Docker 的数据、配置文件和缓存文件。**请注意，这将删除所有 Docker 容器和镜像，以及任何 Docker 生成的数据。在执行这些命令之前，请确保您已备份所有重要数据。**
```
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
sudo rm -rf /etc/docker
sudo rm -rf /etc/systemd/system/docker.service.d
```

5. 如果您在 `/etc/docker/daemon.json` 中添加了自定义配置，请手动删除该文件。

6. 删除所有 Docker 网络接口。这通常不是必需的，但如果您创建了自定义网络，可能需要执行此操作。首先，使用以下命令列出所有 Docker 网络接口：
```
ip link show | grep docker
```
然后，使用以下命令删除每个接口，将 `INTERFACE_NAME` 替换为实际的接口名称：
```
sudo ip link delete INTERFACE_NAME
```

7. 如果您之前添加了任何 Docker 相关的环境变量或配置，请检查 `~/.bashrc`、`~/.bash_profile` 或 `/etc/environment` 文件，并删除这些设置。

8. 最后，重新启动您的系统：
```
sudo reboot
```

现在，Docker 应该已从您的系统上彻底卸载。如果需要，您可以随时重新安装 Docker。

# 镜像

Docker的镜像是一个特殊的文件系统,提供容器运行时所需要的程序,库,资源,配置,以及运行时准备的参数(环境变量,用户)等等,镜像不包含动态数据,构建好后,镜像的内容也不会发生改变

## 分层存储

docker的镜像是由基础镜像一层一层构建过来的,每一层的内容都只可读不可以更改,**这么设计的好处是可以共享镜像**,如果需要更改只能在容器层记录哪些文件被更改了,所有我们尽量把那些需要更改的文件通过容器卷的方式传递给容器,因为容器卷里面的东西不属于镜像,属于宿主机,

## registry

这个就代表镜像所在的仓库

## repository

这个是一组镜像的集合,比如centos镜像的所有版本,所以,repository是镜像的集合,registry是repository的集合

## manifest

主要存在与registry中作为docker镜像的元数据文件,在pull,push,save,load中作为镜像结构与基础信息的描述文件

# 容器

容器其实就是一个进程,但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 命名空间。因此容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全

容器启动时,在镜像的基础上加了一层**容器存储层**,所有的更改操作都进行在这一层,当容器死亡的时候,这一层也将消失

# 常用命令

## pull

拉取一个镜像

```shell
docker pull (地址/仓库/)镜像名字:版本号(没有版本号默认拉取最新版)
```

```
docker pull centos:7
```

## images

查看所有镜像 

```
docker images
```

## image

`docker image` 是 Docker 中用来管理镜像的命令。以下是一些常用的子命令和参数：

1. `docker image ls` 或 `docker images`：列出所有本地镜像。
   - `-a`：显示所有镜像（默认隐藏中间镜像层）。
   - `--digests`：显示摘要信息。
   - `-f` 或 `--filter`：基于给定的条件过滤镜像。
   - `--format`：以指定的格式输出镜像信息。
   - `--no-trunc`：不截断输出。
   - `-q` 或 `--quiet`：仅显示镜像ID。

2. `docker image pull`：从远程仓库拉取镜像。
   - `--all-tags` 或 `-a`：下载仓库中所有标记的镜像。
   - `--disable-content-trust`：跳过镜像的验证。
   - `--platform`：设置平台如果服务器是多平台的。

3. `docker image push`：将本地镜像推送到远程仓库。

4. `docker image rm` 或 `docker rmi`：删除一个或多个镜像。
   - `-f` 或 `--force`：强制删除镜像。
   - `-noprune`：不删除未被使用的父镜像。

5. `docker image build`：构建一个新的镜像。

6. `docker image inspect`：显示一个或多个镜像的详细信息。

7. `docker image history`：显示镜像的历史记录。

以上就是 `docker image` 的一些常用命令和参数，更详细的列表可以通过 `docker image --help` 命令查看。具体使用哪个参数会根据你的实际需求和使用的镜像而有所不同。

## rmi

删除镜像

```shell
docker rmi 镜像名字或者id
docker rmi $(docker images -q)  # 删除所有镜像
```

## run

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

```shell
docker run -it --name centostest centos:7	
```

## exec

在运行的容器中执行命令

```shell
docker exec -it 容器名字/id bash
docker exec -it centostest bash
docker exec centostest ls /
```

* -i 将当前终端输入流给容器
* -t 分配一个终端
* -w 指定工作目录
* -e 指定环境变量
* -u 指定用户

## logs

查看容器后台输出的信息,方便我们纠错

```shell
docker logs centostest
docker logs -f centostest # 实时日志
```

## stop

关闭一个容器  docker stop  id或者名字

```
docker stop centostest
```



## restart

重启一个容器 docker restart id 或者名字

```
docker restart centostest
```



## rm

删掉一个容器

```shell
docker rm -f id或者名字
docker rm -f $(docker ps -aq) #删除所有容器
```

## rename

更改容器的名字

```
docker rename centostest centos7
```

## ps

与linux的ps功能差不多

* docker ps 查看运行的容器
* docker ps -a 查看运行和停止的容器

## commit

将容器打包成镜像(不推荐使用,建议使用build),这个

* --message 打包说明
* --author 作者
* docker commit 容器  (仓库名字)镜像:标签

```
docker commit nginx mynginx:v1
```



## cp

在容器和本地文件系统之间复制文件或文件夹

* docker cp <container_id>:<container_path>  <local_path>  将容器中的内容复制到本地
* docker cp <local_path>  <container_id>:<container_path> 将本地内容复制到容器中

```
docker cp centos7:/root ./test
```

```
docker cp ./test centos7:/root/test
```



## diff

拿容器层与镜像层做对比,看多了哪些,修改了哪些,删除了哪些东西

```
docker diff centos7
```

## inspect

查看容器,网络,镜像,容器卷,网络的详细信息或者说元信息

```
docker inspect 
```



## network

* create -d 类型(一般用bridge,也是默认值) 网络名字 创建一个网络
* rm 删除一个网络
* prune 删除未使用的网络
* connect 将容器加入到某个网络当中去
* disconnect  将容器从某个网络中移除

#### 示例

创建一个网络

```shell
docker network create my-network
```

创建两个容器,使用两种不同的方式加入网络吧

```
docker run -itd --name container1 --network my-network busybox  # 创建的时候就加入网络
```

```
docker run -itd --name container2  busybox
docker network connect my-network container2  # 后面再加入网络
```

进入到container1中ping container2

```
docker exec -it container1 sh
ping container2
```

会发现是可以ping 通的

删除网络

```
docker rm -f container1 container2  # 得先删除属于这个网络的容器,或者移除 
docker network rm my-network
```



#### 答疑

Docker 不会在 `/etc/hosts` 文件中为每个容器添加条目。相反，Docker 使用内置的 DNS 服务器来实现容器之间的名称解析。当您将容器连接到用户定义的网络（如本示例中的 `my-network`）时，Docker 会自动为该网络配置一个内置 DNS 服务器。容器可以使用这个 DNS 服务器来解析其他容器的名称。

在我们的示例中，`container1` 和 `container2` 都连接到了 `my-network`。当您从 `container1` 尝试 ping `container2` 时，`container1` 会向 Docker 内置的 DNS 服务器发送一个 DNS 请求，以解析 `container2` 的 IP 地址。DNS 服务器会返回 `container2` 的 IP 地址，然后 `container1` 可以通过 IP 地址与 `container2` 进行通信。

请注意，这种名称解析功能仅在用户定义的网络中可用。对于默认的桥接网络（`bridge`），容器需要使用 IP 地址进行通信，或者您需要手动更新 `/etc/hosts` 文件以添加容器名称和 IP 地址的映射。这就是为什么建议在需要容器间通信时使用用户定义的网络。

我们可以查看这个网络的信息

```
docker network inspect my-network
```

```json
[
    {
        "Name": "my-network",
        "Id": "aaa94bd17fe571805aa60cdf4ca5dc2ef7252b3ac26b45c4f97861c5303e63aa",
        "Created": "2023-05-03T01:35:46.849865799-07:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "0425b460b23ab302a321987e57f80c0c22ec8d212261fcea2cc1023b62aa44e9": {
                "Name": "container1",
                "EndpointID": "857cca4d333a6989f47a107677e47f720410c3888c098d4f952e0ccb6797f6d2",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            },
            "48bcbe65a098ea7d96feebd0a72a4f731ea8cf475872e0ebaf983ac225af0aa2": {
                "Name": "container2",
                "EndpointID": "1db1fd068f327f11f1df3bc1339b266d030938e95411a8f2bef3db826c3290a9",
                "MacAddress": "02:42:ac:12:00:03",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]

```



## volume 

* create name 创建一个容器卷
* rm name/id 删除一个容器
* ls 列出容器卷
* inspect name/id 查看容器卷的元信息
* prune 删除没有在使用的容器卷(只要有容器挂载,不管是运行的容器,还是停止的容器,都算在使用)



```shell
docker volume create my-volume # 创建一个容器卷

docker volume rm my-volume # 删除,如果有容器挂载了,那么无法删除

docker inspect my-volume # 查看容器卷信息

docker volume ls #列出容器卷

```



## build

基于dockerfile构建一个镜像

```
docker build [OPTIONS] PATH | URL | -
```

- `OPTIONS`：构建镜像时使用的选项。
- `PATH`：Dockerfile 所在的本地路径。通常为当前目录（`.`）。 这个目录就是上下文路径
- `URL`：从远程仓库（如 GitHub）获取 Dockerfile 的 URL。
- `-`：从标准输入（stdin）读取 Dockerfile。

常用的 `docker build` 选项：

1. `-t` 或 `--tag`：为构建的镜像指定一个名称和可选的标签（格式为 `name:tag`）。如果没有指定标签，将使用 `latest` 作为默认标签。示例：`-t myimage:1.0`。
2. `--build-arg`：设置构建参数。这些参数可以在 Dockerfile 中使用 `ARG` 指令定义。示例：`--build-arg API_KEY=myapikey`。
3. `--no-cache`：在构建过程中不使用缓存。默认情况下，Docker 会使用缓存以加速构建过程。
4. `--file` 或 `-f`：指定一个非默认名称或位置的 Dockerfile。**默认情况下，Docker 会在构建上下文路径中查找名为 `Dockerfile` 的文件**。示例：`-f mydockerfile`。
5. `--rm`：在构建过程完成后删除中间容器。默认为 true。
6. `--pull`：尝试从远程仓库拉取基础镜像的新版本，即使本地已经存在该镜像。默认为 false。

示例：

1. **使用当前目录下的 `Dockerfile` 构建一个名为 `myapp` 的镜像**：

   ```
   docker build -t myapp .
   ```

2. **从 GitHub 仓库中的 `Dockerfile` 构建镜像**：

   ```
   docker build -t myapp https://github.com/user/repo.git
   ```

3. 使用名为 `custom.dockerfile` 的文件构建镜像，并设置构建参数：

   ```
   docker build -t myapp --build-arg API_KEY=myapikey -f custom.dockerfile .
   ```

在构建过程中，Docker 会按照 Dockerfile 中的指令逐步执行，并为每个指令创建一个新的层。当所有指令执行完成后，Docker 将构建出一个新的镜像。如果在构建过程中遇到错误，Docker 将返回错误信息，您可以根据错误信息修改 Dockerfile 并重新尝试构建。

## history

查看镜像的构建历史命令

* --no-trunc 查看完整命令(默认只能看到前几个字符)

## tag

可以改变一个镜像的仓库名字,镜像名字,版本号

```shell
docker tag nginx:latest mynginx:v1
```

## export

将一个容器导出成一个文件,但是这么打包出来的镜像,它只会包含一层了,所以不会保存所有的commit记录,比如说你的CMD命令,entrypoint的这些都不会保存,因此在打出的镜像执行的时候需要去重新输入CMD命令才能保证容器继续运行

> export 只能打包容器

格式:  docker export 容器名字或者id -o 打包的名字.tar

```
docker export nginx -o mynginx.tar
```

## import 

将本地或者远程文件导入成镜像

格式:  docker import  打包镜像名字 镜像名字:版本

```shell
docker import ./my-nginx.tar my-nginx:v2
```

这样的镜像直接是运行不了的,需要我们手动输入命令

```shell
docker run -d --name mynginx nginx /docker-entrypoint.sh "nginx" "-g" "daemon off;" 
```

## save 和 load

`docker save` 和 `docker load` 是 Docker 中**用来进行镜像备份和恢复的命令**。

1. `docker save` 命令可以将一个或多个镜像保存为一个 tar 文件，这个 tar 文件可以被传输到其他系统或作为备份存在。其基本的用法如下：

    ```bash
    docker save -o <path for generated tar file> <image name>
    ```

   例如，如果你想将名为 `my_image:latest` 的镜像保存到当前目录下的 `my_image.tar` 文件中，你可以运行以下命令：

    ```bash
    docker save -o my_image.tar my_image:latest
    ```

2. `docker load` 命令可以从一个 tar 文件中加载一个或多个镜像。其基本的用法如下：

    ```bash
    docker load -i <path to image tar file>
    ```

   例如，如果你想从 `my_image.tar` 文件中加载镜像，你可以运行以下命令：

    ```bash
    docker load -i my_image.tar
    ```

这样，你就可以很容易地将 Docker 镜像从一个系统传输到另一个系统，或者在需要时恢复备份的镜像了。如果需要打包容器的话,那还得先commit

## tag

`docker tag` 命令主要用于给 Docker 镜像添加标签。**每个 Docker 镜像可以有多个标签，这些标签用于识别镜像的不同版本或者不同用途。**, 比如如果要上传镜像到服务器, 有时候就要给镜像

# 容器卷



Docker 中的容器卷（Volume）是一种用于**持久化和共享容器数据的机制**。**容器卷独立于容器生命周期，即使容器被删除，卷中的数据仍然存在。容器卷可以被一个或多个容器挂载，以便在容器之间共享数据。**

与直接将宿主机的目录挂载到容器相比，使用容器卷具有以下优点：

1. 数据持久化：容器卷可以在容器之间持久化数据，即使容器被删除，数据仍然存在。
2. 数据共享：容器卷可以被多个容器同时挂载，从而实现数据共享。
3. 容器迁移：容器卷可以方便地在不同的宿主机之间迁移，使得数据迁移变得更加容易。
4. 性能：容器卷通常具有更好的性能，因为它们直接由 Docker 管理。
5. 隔离：容器卷可以提供更好的隔离，因为它们不依赖于宿主机的文件系统结构。



## 容器卷类型

1. **匿名卷（Anonymous volume）：**

   使用 `-v` 时，如果仅提供容器内的路径，Docker 会在宿主机上为卷自动生成一个唯一的 ID，而不是指定的名称。这被称为匿名卷。

   ```
   docker run -v /container/path your_image
   ```

   在这种情况下，Docker 将在容器的 `/container/path` 目录下创建一个匿名卷。由于未指定卷名称，数据将存储在宿主机的 Docker 卷目录下的一个随机目录中。

2. **命名卷（Named volume）：**

   如果同时指定卷名称和容器内路径，就可以创建一个命名卷。命名卷允许您更轻松地引用和管理数据。

   ```
   docker run -v volume_name:/container/path your_image
   ```

   在这种情况下，Docker 将在容器的 `/container/path` 目录下创建一个名为 `volume_name` 的卷。数据将存储在宿主机的 Docker 卷目录下的一个子目录中，该子目录的名称与指定的卷名称相同。

3. **绑定挂载（Bind mount）：**

   如果提供宿主机上的一个路径和容器内的一个路径，就可以创建一个绑定挂载。绑定挂载将容器内的路径映射到宿主机上的路径，从而允许对宿主机上的文件和目录进行读写。

   ```
   docker run -v /host/path:/container/path your_image
   ```

   在这种情况下，Docker 将宿主机上的 `/host/path` 目录映射到容器的 `/container/path` 目录。这意味着在容器内对 `/container/path` 目录的任何更改都会直接反映到宿主机上的 `/host/path` 目录中，反之亦然。

> 不论哪边路径不存在,默认都会创建一个这样的路径,而且宿主机的目录会挂载到容器上,所以,容器对应路径里面的内容是不可见的,不是覆盖了

## 挂在多个容器卷

一个容器可以挂载多个卷，并且可以为每个卷指定权限。您可以使用 `:ro`（read-only，只读）或 `:rw`（read-write，读写）标志为卷指定权限。默认情况下，卷是以读写模式挂载的。

例如，假设您有两个卷：`volume1` 和 `volume2`，您希望将 `volume1` 以只读模式挂载到容器的 `/data1` 目录，将 `volume2` 以读写模式挂载到容器的 `/data2` 目录。您可以使用以下命令：

```
docker run -v volume1:/data1:ro -v volume2:/data2:rw your_image
```

权限问题,当我们使用容器卷的时候,会发现里面的数据我们居然没办法查看,也没有办法创建文件,这个时候,我们需要使用  --privileged=true 创建容器

## 容器卷的迁移

如果您需要在不同机器之间迁移容器卷，可以使用以下方法之一来实现：

**方法一：使用 `docker cp` 命令备份和恢复容器卷数据**

1. 首先，创建一个临时容器，并将要迁移的卷挂载到该容器：

   ```
   docker run -d --name temp_container -v my_volume:/data busybox sleep infinity
   ```

   这里，我们使用了一个名为 `my_volume` 的卷，并将其挂载到了 `/data` 目录。

2. 使用 `docker cp` 命令从临时容器中复制卷数据到宿主机：

   ```
   docker cp temp_container:/data /path/to/backup
   ```

   这将把卷数据复制到宿主机的 `/path/to/backup` 目录。

3. 将备份数据传输到目标机器。您可以使用 `scp`、`rsync` 或其他文件传输工具来实现这一步。

4. 在目标机器上创建一个新的卷：

   ```
   docker volume create my_new_volume
   ```

5. 在目标机器上创建一个新的临时容器，并将新卷挂载到该容器：

   ```
   docker run -d --name new_temp_container -v my_new_volume:/data busybox sleep infinity
   ```

6. 将备份数据从目标机器的宿主机复制到新的临时容器：

   ```
   docker cp /path/to/backup new_temp_container:/data
   ```

7. 最后，删除两个临时容器：

   ```
   docker rm -f temp_container new_temp_container
   ```

**方法二：使用 `docker save` 和 `docker load` 命令备份和恢复带有卷数据的镜像**

此方法适用于卷数据和应用程序代码一起打包在 Docker 镜像中的场景。

1. 使用 `docker save` 命令将镜像导出为 `.tar` 文件：

   ```
   docker save -o my_image.tar my_image
   ```

2. 将 `.tar` 文件传输到目标机器。

3. 在目标机器上使用 `docker load` 命令导入镜像：

   ```
   docker load -i my_image.tar
   ```

注意：这两种方法都需要手动备份和恢复容器卷数据。在迁移过程中，务必确保不会丢失任何数据。根据您的需求和环境，选择最适合您的方法。

# 构建镜像

## commit

当我们使用commit 之后,是将**当前容器的存储层+原来的镜像打包成一个新的镜像**,这样容器的存储层就会被保留下来,后面也无法再更改,如果我们使用了卷的话,这个东西并不属于存储层,自然不会被保存

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

#尽量不要使用docker commit 来制作镜像,这样不利于我们使用分层镜像,而且也不利于修改镜像,每一次commit都要在原有的基础上新增,而如果使用build的话,可以充分利用以前的镜像分层, 还有就是commit的话是不知道我们在容器的基础上干了些什么的
```

### 注意点

- `docker commit` **不会保存容器的运行状态，只会保存文件系统状态和部分配置**，比如环境变量等。
- 默认情况下，新镜像会保留原始镜像的 `CMD` 和 `ENTRYPOINT` 指令。如果需要，可以使用 `-c` 或 `--change` 选项来修改这些指令。
- `docker commit` 不会保留镜像的构建历史和构建上下文。**也就是说看不到对容器执行了哪些命令,影响了哪些文件**

## dockerfile

### 常用配置项

抱歉刚刚没有详细列出 Dockerfile 的所有配置项。以下是 Dockerfile 中的一些主要指令及其用途：

1. `FROM`: 指定基础镜像。例如：`FROM ubuntu:20.04`。
2. `LABEL`: 添加元数据标签，如维护者信息。例如：`LABEL maintainer="your_name <your_email@example.com>"`。
3. `RUN`: 执行命令，用于安装软件包、更新配置文件等。例如：`RUN apt-get update && apt-get install -y nginx`。
4. `CMD`: 设置容器启动时运行的默认命令。如果在 `docker run` 时传递了参数，`CMD` 中的命令将被覆盖。例如：`CMD ["nginx", "-g", "daemon off;"]`。
5. `ENTRYPOINT`: 设置容器启动时运行的命令，与 `CMD` 类似，但不会被 `docker run` 时传递的参数覆盖。例如：`ENTRYPOINT ["nginx", "-g", "daemon off;"]`。
6. `COPY`: 将本地文件复制到镜像中。例如：`COPY index.html /var/www/html/`。**这里本地文件可以使用相对路径,相对上下文路径来说**
7. `ADD`: 与 `COPY` 类似，但可以在复制之前执行解压操作。例如：`ADD myapp.tar.gz /app/`。
8. `WORKDIR`: 设置镜像中的工作目录。例如：`WORKDIR /app`。
9. `ENV`: 设置环境变量。例如：`ENV MY_VAR=my_value`。
10. `EXPOSE`: 声明容器需要监听的端口。例如：`EXPOSE 8080`。**告诉别人我内部使用了什么端口,好让别人运行这个容器的时候做端口映射**
11. `USER`: 设置运行容器的用户。例如：`USER myuser`。
12. `VOLUME`: 定义匿名卷，用于数据持久化和共享。例如：`VOLUME /var/lib/mysql`。**告诉别人我内部有哪里的数据是可以使用容器卷的,让别人指定容器卷,然后保留容器运行产生的数据**
13. `ARG`: 定义构建时变量，可以在 `docker build` 命令中使用 `--build-arg` 参数设置。例如：`ARG MY_BUILD_ARG`。
14. `ONBUILD`: 为基础镜像添加触发器，在其他镜像中使用该基础镜像时触发。例如：`ONBUILD RUN echo "Hello from base image"`。
15. `STOPSIGNAL`: 设置停止容器时发送的信号。例如：`STOPSIGNAL SIGQUIT`。
16. `SHELL`: 设置运行 `RUN`, `CMD` 和 `ENTRYPOINT` 指令时使用的默认 shell。例如：`SHELL ["/bin/bash", "-c"]`。

### 注意点

Dockerfile 是一个文本文件，其中包含了一系列用于构建 Docker 镜像的指令。编写 Dockerfile 时，需要注意以下几点：

1. 从基础镜像开始：使用 `FROM` 指令来指定基础镜像。例如：`FROM ubuntu:20.04`。
2. 标签：为了便于维护和版本控制，尽量使用具体的基础镜像标签，而不是 `latest`。
3. 维护者信息：使用 `LABEL` 指令添加维护者信息。例如：`LABEL maintainer="your_name <your_email@example.com>"`。
4. 运行命令：使用 `RUN` 指令来执行安装软件包、更新配置文件等操作。避免在一个 `RUN` 指令中执行过多操作，以免产生过大的镜像层。另外，可以使用反斜杠（`\`）在多行书写这些命令以提高可读性。
5. 分层：**合理安排 Dockerfile 中的指令顺序，将经常变动的部分放在底部，以便充分利用镜像缓存**。
6. 复制文件：使用 `COPY` 和 `ADD` 指令将本地文件复制到镜像中。尽量使用 `COPY`，因为它更简单，只复制文件；而 `ADD` 在复制文件之前还可以执行解压操作。
7. 工作目录：使用 `WORKDIR` 指令设置镜像中的工作目录。这会影响后续指令的相对路径。
8. 设置环境变量：使用 `ENV` 指令设置环境变量。例如：`ENV MY_VAR=my_value`。
9. 暴露端口：使用 `EXPOSE` 指令声明容器需要监听的端口。例如：`EXPOSE 8080`。
10. 设置用户：使用 `USER` 指令设置运行容器的用户，以避免使用 root 用户运行应用程序。例如：`USER myuser`。
11. 容器启动命令：使用 `CMD` 或 `ENTRYPOINT` 指令设置容器启动时运行的命令。`CMD` 可以被 `docker run` 时传递的参数覆盖，而 `ENTRYPOINT` 则不会。

为了更好地编写 Dockerfile，请注意以下几点：

- **保持 Dockerfile 简洁：删除不必要的指令，减少镜像层数**。
- 使用多阶段构建：通过使用多个 `FROM` 指令，可以将构建过程分为多个阶段，以减小最终镜像的大小。
- 避免使用 `sudo`：Dockerfile 中的指令默认以 root 用户身份运行，因此不需要使用 `sudo`。
- **清理缓存：**在安装软件包或执行其他操作时，确保在同一个 `RUN` 指令中清理不必要的缓存文件，以减小镜像大小。例如，在使用 `apt-get` 安装软件包后，可以运行 `apt-get clean` 和 `rm -rf /var/lib/apt/lists/*` 来清理缓存。
- **避免在容器中运行 SSH**：尽量不要在容器中运行 SSH 服务，因为这会增加安全风险。取而代之的是，使用 `docker exec` 命令来进入正在运行的容器。
- **使用 `.dockerignore` 文件**：创建一个 `.dockerignore` 文件以排除不需要复制到镜像中的文件，从而减小镜像大小。
- 文档和注释：在 Dockerfile 中添加必要的注释和文档，以提高可读性和可维护性。
- 定期更新和审查：定期更新基础镜像、软件包和配置，以确保容器始终运行在最新且安全的环境中。同时，定期审查 Dockerfile，以确保其符合最佳实践。

```shell
# dockerfile 的编写

ARG 设置环境变量(放在FROM前面,变量只能在所有FROM里面使用,放在其他指令前面,只有那一个指令能用)
FROM 基础镜像(名字:版本号)  (scratch 空镜像)
ENV 设置环境变量(到时候容器里面会存在这个变量哦)
RUN 命令   
CP 源路径(相对于上下文来说) 目标路径(可以相对于容器来说,也可以相对于容器里面的工作目录(通过WORKDIR指定来说)
ADD 压缩包路径(相对于上下文) 目录路径(同上)  add 可以做其他的事(和cp一样的功能,下载文件),但是推荐只做这个事情
CMD ["可执行文件","参数"] 容器启动时默认执行命令,当然我们自己写的命令会替换掉这个,CMD里面的命令会最终被替换成sh -c "可执行文件","参数"
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







## 对比

`docker commit` 和 `docker build` 都用于创建 Docker 镜像，但它们之间存在一些关键差异。以下是它们之间的对比：

1. **构建过程**：

   - `docker commit`：从现有的容器创建新的镜像。首先，您需要启动一个容器，对其进行更改（例如安装软件或修改配置文件），然后使用 `docker commit` 命令将这些更改保存到新的镜像。

   - `docker build`：使用 Dockerfile 描述的一系列指令来创建镜像。Docker 会根据 Dockerfile 中的指令自动执行容器的更改、提交和删除。这为镜像构建过程提供了自动化和可重复性。

2. **可重复性和可维护性**：

   - `docker commit`：**手动执行更改和提交可能导致不一致和难以追踪的结果。当需要修改镜像时，您需要记住并手动执行所有更改和提交。**

   - `docker build`：Dockerfile **提供了一种声明式的方式来描述镜像构建过程。这使得在不同环境中构建相同镜像变得简单，也有助于团队成员之间共享构建过程。此外，当需要修改镜像时，可以轻松地查看和编辑 Dockerfile。**

3. **层次结构和缓存**：
- `docker commit`：当您使用 `docker commit` 创建镜像时，所有更改都会保存在单个镜像层中。这可能导致较大的镜像和较低的缓存效率。
  
- `docker build`：`docker build` 会为 Dockerfile 中的每个指令创建一个新的镜像层。这有助于更好地管理镜像的大小和缓存。例如，如果只更改了 Dockerfile 中的一个指令，那么 Docker 只需要重新构建该指令对应的层，而无需重新构建整个镜像。这有助于加速构建过程。

总的来说，虽然 `docker commit` 可以用于从现有容器创建新镜像，但在大多数情况下，建议使用 `docker build` 和 Dockerfile 来构建镜像。这样可以确保镜像构建过程的可重复性、可维护性以及更高效的层次结构和缓存管理。



# docker-compose

这个东西是用来管理docker容器的,那么多docker容器,难道我们每次部署都要去一一启动并且配置吗?那多麻烦,得用docker-compose去管理

##  安装

```shell
curl -L https://get.daocloud.io/docker/compose/releases/download/v2.4.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
#赋予权限
chmod o+x /usr/local/bin/docker-compose
```

配置好自动自动补全

```shell
$ curl -L https://raw.githubusercontent.com/docker/compose/1.27.4/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose
```

## 卸载

```shell
rm -f /usr/local/bin/docker-compose
```

## 常用命令

​	我们使用docker-compose的时候可以指定一些参数

* -f 指定docker-compse.yml的位置(默认就在当前目录) 
* -p 指定项目名字(默认就是目录名字)

> docker-compose只有在具有docker-compose.yml目录下使用才有用(**除非指定docker-compse.yml的位置**),否则会提示
> no configuration file provided: not found

### build

构建项目中的镜像,就是构建在配置文件中使用了build配置项的服务,如果有的话,则会构建一个镜像到仓库中,默认名字是当前目录名字+service对应的名字

### config

检查配置文件是否正确,正确则显示完整配置文件,否则说明错误原因

### down

删掉项目中通过up启动的服务,并且删除网络

### exec

进入项目中的容器

### images

列出compose文件中启动的容器对应的镜像

### kill

杀掉一个项目中的服务(得使用服务名字哦)

### stop

停止一个服务

### up

这个命令巨屌好吧,帮我们省了不少事,它将尝试自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作

### scale

指定开启服务个数,如果服务多于这个就停止,少了就增加 

## docker-compose.yml 模板

### build

如果镜像存在则不会构建镜像,否则根据指定文件夹路径(可以是相对docker-compose.yml的路径,也可以是绝对路径)构建镜像,构建镜像的名字为当前docker-compose 文件所在目录的目录名+服务名字版本为最新版本,子命令

* context 指定dockerfile的位置

### command

覆盖容器启动的时候执行的命令,也就是相当于在dockerfile后面多加一条CMD

### devices

设备映射关系

```yml
devices:
  - "/dev/ttyUSB1:/dev/ttyUSB0"
```

### depends_on

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

### dns

指定DNS服务器,可以是单个数据,也可以是列表

### environment

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

### expose

暴露端口,但是不映射,互联在一个网络中的容器可以访问

```yaml
expose:
 - "3000"
 - "8000"
```

### extra_hosts

```yaml
extra_hosts:
 - "mysql:123.323.12.12"
```

这个时候/etc/hosts下面会多

```
123.323.12.12 mysql
```

### healthcheck

通过命令检查容器是否健康运行。

```yaml
healthcheck:

  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 1m30s
  timeout: 10s
  retries: 3
```

### image

指定为镜像名称或镜像 ID。如果镜像在本地不存在，Compose 将会尝试拉取这个镜像,用这个镜像启动作为容器

### logging

配置日志

### port 

与docker run -p 里面的作用是差不多的

# 额外补充



## build使用缓存问题

Docker 使用镜像层的概念来构建和存储镜像。在构建过程中，Docker 会根据 Dockerfile 中的每个指令创建一个新的镜像层。每个层都会在前一个层的基础上应用更改。**Docker 使用内容寻址的方式来存储这些层，这意味着每个层都有一个唯一的哈希值，该哈希值取决于层的内容。**

**当 Docker 遇到一个已经构建过的指令时，它会检查该指令对应的缓存层是否存在。如果存在，Docker 将直接使用该缓存层，而无需重新构建。这可以显著加速构建过程。Docker 根据指令内容和上下文来确定缓存层的有效性。**

当您在 Dockerfile 中新增一条指令时，Docker 将从头开始执行 Dockerfile。在遇到新增指令之前，Docker 会尝试使用之前构建过程中产生的缓存。一旦到达新增指令，Docker 将根据该指令创建一个新的层。此时，Docker 会重新构建该指令之后的所有层，因为它们取决于新增指令所创建的层。

简而言之，Docker 通过镜像层的唯一哈希值来记住缓存，这些哈希值取决于指令内容和上下文。当 Dockerfile 更改时，Docker 会尽可能使用现有的缓存，但在遇到更改点时，它将重新构建受影响的层。这样可以确保构建出的镜像始终是最新的。

## export 和 import注意点

首先，`export` 和 `import` 命令在 Docker 中的用途主要是将容器的文件系统导出到 tar 归档文件中，然后再将这个 tar 文件导入到 Docker 以创建一个新的镜像。它并不包含完整的镜像信息，例如环境变量，用户，工作目录，入口点等。**这些信息在 Dockerfile 中被定义，但并不会被保存到 tar 文件中。例如容器的元数据（如CMD，ENTRYPOINT，ENV等）并不会被导出和导入**, 因此，当你从导入的镜像启动一个新的容器时，可能需要手动指定这些参数。



# 遇到的坑

* 开启或者关闭防火墙后,一定要重启docker,不然会报错
* 如果挂载好容器卷发现在容器里面无法访问数据,权限出问题,那大概率是selinux没有设置成disabled   修改/etc/selinux/config 里面的SELINUX为disabled

* **Failed to get D-Bus connection: Operation not permitted** ,Docker的设计理念是在容器里面不运行后台服务，容器本身就是宿主机上的一个独立的主进程，也可以间接的理解为就是容器里运行服务的应用进程。一个容器的生命周期是围绕这个主进程存在的，所以正确的使用容器方法是将里面的服务运行在前台。但是要在容器里面运行一个服务也不是不可以,创建容器的时候使用 /usr/sbin/init作为启动执行命令,然后加入--privileged=true

  ```shell
  docker run -id -p 8081:22 --name centos7 --privileged=true  centos:7 /usr/sbin/init
  ```

  

## daemon.json

这里面的东西必须严格按照json规范,什么逗号多一个都不行
