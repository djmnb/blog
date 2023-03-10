---
title: hexo部署到远程服务器
date: 2022/11/24 12:23
tags: 
 - hexo 
 - docker 
categories:
comments: true

---

# hexo+git+docker/nginx

怎么安装,这些就自行百度,或者关注我之后的博客

# 服务器端

## 创建一个用户

由于需要使用到ssh免密操作,所有不好直接把公钥放到root用户下,新建一个用户来管理(当然,你也可以用root用户)

```shell
useradd git
# 将本地创建好的公钥放到/home/git/.ssh/authorized_keys 里面,这样就能免密登录了
mkdir /home/git/.ssh
vim  /home/git/.ssh/authorized_keys  #输入你的秘钥
# 设置不能通过git用户登录服务器,但是可以使用git操作仓库
vim /etc/passwd
# git:x:1002:1002::/home/git:/usr/bin/git-shell  只需要将/bin/bash 改成 /usr/bin/git-shell 这个就好了 ,需要改成自己git-shell的路径哦,每个人的git环境路径可能是不一样的
```

##  搭建git服务器

```shell
# 在服务器上搭建一个裸仓库,用来当git服务器,目录自己选
git init --bare /opt/git/repository 
# 将目录所有者给git
chown -R git:git /opt/git 
```

## 编写post-update钩子

方便我们推送文章后,自动让另一个服务器本地仓库更新页面

```shell
# 将钩子变的可用
mv /opt/git/repository/hooks/post-update.sample /opt/git/repository/hooks/post-update
# 清空钩子内容
echo "" > /opt/git/repository/hooks/post-update
# 编写git服务器的post-update钩子
vim /opt/git/repository/hooks/post-update


#################将下面的脚本全部复制进去######################

#!/bin/sh
# 服务器给web服务器访问的博客目录
blogpath=/opt/git/blog
# git服务器地址
repositorypath=/opt/git/repository
# 如果博客还不存在,则先clone,如果存在直接拉取
if [ ! -d $blogpath ]; 
then
  # 克隆好服务器本地仓库
  git clone $repositorypath $blogpath
else
  # 让本地仓库拉取本地远程仓库
  git --work-tree=$blogpath --git-dir=$blogpath/.git pull -f
fi

```

## 设置web服务器

### 方式一  nginx

现在我们已经有了所有的静态资源在/opt/git/blog/public目录下,我们只需要把这个目录交给web服务器就行,设置nginx的根目录为这个目录就行了

```shell
vim /etc/nginx/nginx.conf  # 每个人的环境变量不一样哦,注意自己安装在哪

listen       80;
listen       [::]:80;
server_name  _;
root        /opt/git/blog/public;

#改成这样就OK啦

```

### 方式二 docker

```shell
docker run -d --name hexonginx -v /opt/git/blog/public:/usr/share/nginx/html -p 80:80 nginx
```

这个是不是巨方便啊,哈哈哈哈

# 客户端

## 创建本地博客仓库

```shell
# 自己选好路径
git init 
# 添加远程仓库,上面写好的,这里的ip需要写成服务器ip地址哦
git remote add origin git@ip:/opt/git/repository 
# 添加Gitee 仓库地址 主要也是做个备份,安全起见,万一哪天服务器不小心rm -rf / 了,那我不得哭死啊
git remote add gitee git仓库地址
```

编写好.gitignore文件 我们只需要配置文件,以及source,public,其他的基本都不需要,下面是gitignore文件

```shell
.DS_Store
Thumbs.db
db.json
*.log
.deploy*/
_multiconfig.yml
themes
node_modules
```

## 编写好钩子

在.git/hook下面

编写一个pre-commit 文件,不要带任何后缀

```shell
#!/bin/sh
# 自动生成html文件
hexo g
#自动暂存(主要是为了将那些新创建的文件给添加到暂存区,不然commit -a 也没用)
git add .
echo "添加到暂存区完成"
```

编写一个post-commit 文件,不要带任何后缀

```shell
#!/bin/sh
echo "开始推送"
git push gitee master
echo "推送到gittee成功"
git push origin master
echo "推送到自己服务器成功"
```

## 推送

```shell
#当我们在source/_post目录下写好文章之后
#直接commit
git commit -am "终于完成了"
```

