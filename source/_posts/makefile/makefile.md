---
title: makefile学习
date: 2023-10-2
tags:
  - makefile
---

# 前言

## 什么是 Makefile？

`Makefile` 是一个用来自动化构建项目的简单工具，通常用在编译和链接程序的过程中，但它也可以用来执行任何你想自动化的任务。`Makefile` 包含一系列规则和指令，它们定义了如何构建项目和执行其他相关任务。

## 为什么使用 Makefile？

1. **自动化：**`Makefile` 可以自动化许多编程任务，比如编译源代码、生成文档、或执行测试等。
2. **依赖跟踪：**`make` 工具可以自动检测文件之间的依赖关系，只重新构建实际需要更新的部分，而不是整个项目。
3. **跨平台：**虽然 `make` 最初是为 Unix 和类 Unix 系统开发的，但现在也可用于许多其他操作系统。

## Makefile 的基本组成

1. **目标（Target）:** 是你想完成的任务名称。比如：编译源代码可以是一个目标。
2. **依赖（Dependencies）:** 是完成任务所需的前置条件，通常是源文件或其他目标。
3. **命令（Commands）:** 是 `make` 执行的实际命令，它们指定了如何从源文件创建目标输出。
4. **伪目标(Phony target)**: 伪目标并不代表实际的文件名，**而是一个执行特定任务的标签名称**。伪目标没有对应的文件名，并且它的命令总是被执行的, **主要是为了避免和文件同名然后不执行的情况**。 可以通过**.PHONY: clean** 这样 指定

我们需要将目标的名字设置成有用的,真实的目标的名字  以及 依赖也需要写上,  这样的话,Makefile会帮我们做检查,  看是否需要生成, 这样的话, 对于大型项目,  编译 构建的效率就非常高

# Makefile 变量

Makefile 中的变量是其强大功能之一，它们使得 Makefile 更具有模块化和可维护性。以下是 Makefile 中常见的变量及其简短总结：

1. **简单变量赋值 (`=`)**:
   ```make
   VARIABLE = value
   ```
   **这种赋值是递归的**，右边的 `value` 在每次引用 `$(VARIABLE)` 时都会重新被评估。(**这里指的是,如果在后面修改了VARIABLE 这里的的值,  这样的话,  前面使用了这个变量的话也会变成这个值**)  **相当于引用赋值**

   ```
   value = djm
   value2 = $(value)
   showValue:
   	# 这里的value2变成了 djm666
   	echo $(value2)  
   value = djm666
   ```
   
2. **立即变量赋值 (`:=`)**:
   ```make
   VARIABLE := value
   ```
   右边的 `value` 仅在赋值时评估一次。

   ```
   value = djm
   value2 := $(value)
   showValue:
   	# 这里的value2 不会变成了 djm666   还是 djm
   	echo $(value2)  
   value = djm666
   ```
   
   
   
3. **追加赋值 (`+=`)**:
   ```make
   VARIABLE += value
   ```
   这种方式会将 `value` 追加到现有的 `VARIABLE` 值后面。

4. **条件变量赋值 (`?=`)**:
   ```make
   VARIABLE ?= value
   ```
   只有当 `VARIABLE` 未定义或为空时，才会赋值。

5. **自动化变量**:
   - `$@`: 代表规则的目标文件名。
   - `$<`: 代表规则的第一个依赖文件名。
   - `$^`: 列出所有的依赖文件，避免列出重复的依赖。
   - `$+`: 类似 `$^`，但包括所有依赖，包括重复的。
   - `$*`: 代表目标文件名中的基本部分（没有扩展名或路径）。

6. **预定义变量**:
   例如:
   - `CC`: C编译器，默认为 `cc`。
   - `CXX`: C++编译器，默认为 `g++`。
   - `AR`: 创建库的程序，默认为 `ar`。
   - `RM`: 删除文件的程序，默认为 `rm -f`。
   以上仅仅是其中的一部分预定义变量。

7. **环境变量**:
   所有的环境变量都被导入到 Makefile 中，并可以被直接引用。例如，`PATH` 环境变量在 Makefile 中可以使用 `$(PATH)` 来引用。

8. **函数**:
   Makefile 支持各种字符串、文件名和其他函数来操作和转换变量的值。例如:
   ```make
   OBJECTS := $(patsubst %.c,%.o,$(SOURCES))
   ```

在使用 Makefile 的过程中，正确地使用和理解这些变量对于编写强大、可维护的构建规则至关重要。

使用变量的格式:

* $(变量名字)
* ${变量名字}  

# Makefile 函数

`Makefile` 中包含了一系列的函数，它们提供了字符串操作、文件名操作、条件判断等功能。以下是一些常用的 `Makefile` 函数及其简短描述：

1. **字符串函数**:
    - `$(subst from,to,text)`: 在文本 `text` 中替换字符串 `from` 为 `to`。
    - `$(patsubst pattern,replacement,text)`: 模式字符串替换。
    - `$(strip string)`: 去除 `string` 开头和结尾的空白。
    - `$(findstring find,text)`: 在 `text` 中查找 `find`，如果找到，则返回 `find`，否则返回空。
    - `$(filter pattern...,text)`: 返回与模式匹配的词。
    - `$(filter-out pattern...,text)`: 返回与模式不匹配的词。
    - `$(word n,text)`: 返回 `text` 中的第 `n` 个词。

2. **文件名函数**:
    - `$(dir names...)`: 返回文件名的目录部分。
    - `$(notdir names...)`: 返回非目录部分的文件名。
    - `$(suffix names...)`: 返回文件名的后缀。
    - `$(basename names...)`: 返回不带后缀的文件名。
    - `$(addsuffix suffix,names...)`: 添加后缀到文件名。
    - `$(addprefix prefix,names...)`: 添加前缀到文件名。

3. **控制函数**:
    - `$(foreach var,list,text)`: 为 `list` 中的每个单词求值一次 `text`。
    - `$(if condition,then-part[,else-part])`: 如果 `condition` 为真，则求值 `then-part`，否则求值 `else-part`。
    - `$(or condition...)`: 如果至少有一个 `condition` 为真，返回第一个为真的 `condition`。
    - `$(and condition...)`: 如果所有 `condition` 都为真，返回最后一个 `condition`。

4. **其他函数**:
    - `$(wildcard pattern)`: 返回与模式匹配的所有文件名。
    - `$(realpath names...)`: 返回文件的绝对路径。
    - `$(abspath names...)`: 返回文件的绝对路径，但不解析符号链接。
    - `$(shell command)`: 执行 shell 命令并返回其输出。
    - `$(call var,param,param,...)`: 使用参数扩展变量。

5. **计算函数**:
    - `$(value var)`: 获取变量的值而不是扩展它。
    - `$(eval text)`: 评估 `text` 作为 `make` 代码。
    - `$(origin variable)`: 返回变量的定义来源。

以上仅列出了 `Makefile` 中的常用函数，实际上还有更多功能和更详细的参数选项。使用这些函数可以帮助你编写更加复杂和灵活的构建规则。

# 补充

## 注意点

1. **`@` 符号**：它告诉 `make` 在执行命令时不显示命令。

    ```make
    all:
    	@echo This will be printed without showing the command.
    ```

2. **`-` 符号**：放在命令前面，它告诉 `make` 即使命令失败也要继续执行。默认情况下，`make` 会在命令失败时停止。

    ```make
    all:
    	-false
    	@echo This will still be printed even though the command above failed.
    ```

3. **`+` 符号**：如果你使用了 `.ONESHELL` 特性或使用了 `make -e` 选项，这会导致 `make` 用单个 shell 执行整个脚本。`+` 符号可以强制某个命令在它自己的 shell 中执行。

4. **自动变量**：例如 `$@`, `$<`, `$^` 等。这些变量在规则的命令中都有特定的值，用于引用目标和依赖项。

5. **变量引用**：在 `Makefile` 中，你使用 `$(VARIABLE_NAME)` 或 `${VARIABLE_NAME}` 来引用变量。

6. **多行命令**：如果你需要一个目标执行多个命令，每个命令都必须独立且前面有一个制表符（tab），不是空格。

    ```make
    all:
    	@echo First command.
    	@echo Second command.
    ```

7. **制表符 vs 空格**：这可能是新手最常遇到的问题。在目标的命令前，你必须使用制表符（tab），而不是空格。否则，`make` 会报错。

8. **命令组合**：如果你想在单行上执行多个命令，你可以使用分号 `;` 或逻辑运算符 `&&` 和 `||`。

    ```make
    all:
    	@echo First command. ; echo Second command.
    ```

这些只是使用 `Makefile` 时需要注意的一些细节和特性。为了编写高效且没有错误的 `Makefile`，通常需要对 `make` 的更多特性和细节有深入的了解。