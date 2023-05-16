---
title: windows常用命令
date: 2023-5-16
tags:
  - 命令总结
categories:
  - windows
---

# 前言

有时候需要用到windows命令,每次都要谷歌查一下,下一次还要继续查, 又不能保证每次都能查到,我索性总结一下

# 查看信息命令

## 查看端口是否被占用

```
netstat -ano | findstr port(端口)
```

