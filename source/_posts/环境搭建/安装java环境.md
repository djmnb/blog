## centos7安装java

### yum安装

```shell
# 先看有哪些jdk的版本
yum search jdk  
# 安装1.8这个版本
yum install -y java-1.8.0-openjdk.x86_64
# 上面安装完成后是没有javac的,还需要安装一个东西
yum install java-devel
```

