---
title: yaml语法
date: 2022-12-20
categroies:
  - 工具
---

## 概述



## 基本语法

* 使用空格作为缩进
* 缩进空格数量不做要求,但是相同层级的左侧元素要对齐
* 低版本的不允许使用tab缩进,只能用空格
* 使用#做注释符,从字符到行尾,都算注释
* 使用 -- 表示新的yaml文件开始

## yaml支持的数据结构

对象

```yaml
person:
	name: djm
	age: 18
```

数组

```yaml
names:
	- djm
	- lpb
```

```yaml
names: [djm, lpb]
```

