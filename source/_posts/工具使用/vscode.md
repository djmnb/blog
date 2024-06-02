---
title: vscode的使用
date: 2023-10-5
tags:
  - 工具
---

# 前言

这里主要介绍一些配置项和好用插件

# 外观

## 主题选择

### 文件主题

* vscode-icons
* Material Icon Theme

# 插件

# 运行和调试

vscode  是通过 配置launch.json  和  task.json 来  进行调试和 运行程序

## python配置

```
{
  // 使用 IntelliSense 了解相关属性。
  // 悬停以查看现有属性的描述。
  // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python 调试程序: 当前文件", // 当前配置名字
      "type": "debugpy", // 类型
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "cwd": "${fileDirname}",
      "python": "C:\\Users\\asus\\miniconda3\\envs\\ML\\python.exe", // 默认使用vscode底部选用的python
      "env": {
        "PYTHONPATH": "${fileDirname}" // 我们需要将当前工作目录加到python包寻找路径里面,可以寻找到我们的包
      }
    }
  ]
}

```

