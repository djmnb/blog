---
title: windows程序设计
date: 2024-5-8
tags:
  - windows
---

# 基础知识

## 字符集

我觉得字符集这里要分为两个部分:

1. 字符集编码: 一个字符对应一个数字值, 不同的字符集对应的编码是不一样的 比如 ascll 编码 和 Unicode 和 ansi
2. 编码方案:  如何转换计算机里面的字节数据到编码 比如 Unicode的转换就有 UTF-8 UTF-16 UTF-32 

asni编码 根据不同国家对应的编码方案是不同的, 字符集也不同

## 字符和宽字符

宽字符使用Unicode编码 统一两个字节 字符的话一般使用多字节编码ansi

```
wchar* "c语言"  // 在Unicode下面这个是8字节
char* "c语言" // 在ansi  里面是6字节 c一个 \0 一个 其他都是双字节
```

注意区分代码编码  和 变量本身编码  这是两个不同的东西,  代码的编码取决于你的选择, 但是变量的编码一般不是你决定的,  但是你的代码编码会影响到变量里面的值

比如 你的代码文件采用的是asni  但是对于 wchar* "c语言"  文件里面它是6字节  但是内存里面它是8字节 (可以这样理解),  如果代码文件编码与变量编码不一致 就会出现很大的问题了没准 "c语言" 就变成其他东西饿了

### TCHAR 

windows为了可以使用这个东西 实现程序的两套编码版本,  一个是ansi 一个是 Unicode  

```
#ifdef  UNICODE
    typedef WCHAR  TCHAR, *PTCHAR;
#else
    typedef CHAR   TCHAR, *PTCHAR;
#endif
```

搭配TEXT宏就很完美

```
#ifdef  UNICODE
    #define __TEXT(quote) L##quote
#else
    #define __TEXT(quote) quote
#endif

#define  TEXT(quote)  __TEXT(quote)
```

这样就演化出不同的字符串指针

```
typedef char CHAR;

typedef _Null_terminated_ CHAR          *NPSTR, *LPSTR, *PSTR;
typedef _Null_terminated_ CONST  CHAR   *LPCSTR, *PCSTR;

typedef _Null_terminated_ WCHAR         *NWPSTR, *LPWSTR, *PWSTR;
typedef _Null_terminated_ CONST  WCHAR  *LPCWSTR, *PCWSTR;

#ifdef  UNICODE
    typedef LPWSTR   PTSTR,  LPTSTR;
    typedef LPCWSTR  PCTSTR, LPCTSTR;
#else
    typedef LPSTR    PTSTR, LPTSTR, PUTSTR, LPUTSTR;
    typedef LPCSTR   PCTSTR, LPCTSTR, PCUTSTR, LPCUTSTR;
#endif
```

所以我们尽量使用 TCHAR 变量类型   TEXT 转换字符串字面值  LPTSTR LPCTSTR(常量) 字符串指针 

> 对于 PTSTR  和 LPTSTR  是为了兼容以前的版本  以前有长指针 和 指针的区别  现在都一样了

### 字符串函数

为了让wchar和char使用字符串函数使用起来统一 Windows提供了很多  _t 开头的函数 比如 _tprintf  _tcscat_s  等等