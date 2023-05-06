---
title: thinking in java
catogories:
  - 书籍阅读
tags:
  - java
---



# 第一章 对象入门

拟出一个计划

首先我们应该要明白我们的程序需要做什么,而不是考虑程序要怎么做,我们应该将重心放到这一阶段的核心问题上,不要纠结与一些细枝末节,同时也不要过分在意系统的**"完美"**,否则容易产生挫败感和焦虑情绪

对自己的系统做一些**"名词"**和**"动词"**的描述,名词成为自然对象,动词成为对象接口中的方法

根据自己的经验与直觉,对一个项目进行日程估计,然后在这个时间上再加上百分之十,如果按时完成了,那么这个百分之十的时间,可以用来完善项目



如何构建计划呢? 通常建议使用UML很好





```
{
    int x;
    {
        int x; //在java里面,这个是非法的
    }
}
```



**java的包名命名规范一般是域名倒着来,首先,我们是想包名唯一,正好域名是唯一的,但是域名后两个是固定的,前面又可以随便变化,所以域名符合要求**,而且我们为了方便管理,还要把域名倒过来才行,假如我有个域名 djm.com  那么 ww.djm.com,abc.djm.com  不都是我的子域名么,如果正着来,不好管理啊,反着来,前面都一样,好管理

@Override 是重写  发生在子父类之间(同名,同参数,而且子类访问权限不能小于父亲,子类异常也要是父类的异常的子类)

@Overload 是重载  发生在本类中(同名,不同参数)

# 第二章 一切都是对象

堆里面存放对象句柄,也就是对象的内存地址, 而堆里面存放对象

## 堆和栈

在 Java 中，堆（Heap）和栈（Stack）是两种不同的内存区域，它们在内存分配和数据存储方面有着本质的区别。下面是它们之间的一些主要差异：

1. 存储内容：
   堆：主要存储对象实例和数组。
   栈：主要存储基本类型变量（如 int、float、boolean 等）及对象引用变量。

2. 内存分配：
   堆：**在运行时动态分配内存**，根据需要申请和释放内存空间。内存分配速度相对较慢。
   栈：**在编译时静态分配内存**，随着方法的调用和返回而自动分配和释放内存空间。内存分配速度较快。

3. 生命周期：
   堆：堆中的对象实例的生命周期取决于垃圾回收器。当对象不再被引用时，垃圾回收器会自动回收其占用的内存。
   栈：栈中的数据的生命周期与方法调用和返回的生命周期相对应。当方法返回时，其栈帧（包含局部变量和引用变量）会自动销毁。

4. 访问速度：
   堆：相对较慢，因为堆是在运行时动态分配内存。
   栈：相对较快，因为栈是在编译时静态分配内存。

5. 内存管理：
   堆：由垃圾回收器负责管理内存，对于不再使用的对象实例进行回收。
   栈：内存管理相对简单，随着方法的调用和返回自动分配和释放内存空间。

6. 容量大小：
   堆：堆的容量通常比栈大得多，因为它需要存储所有创建的对象实例和数组。
   栈：栈的容量相对较小，通常只存储局部变量和引用变量。

总之，堆和栈在 Java 中扮演着不同的角色，它们各自负责存储不同类型的数据和管理内存。了解它们的区别有助于编写更高效、更可靠的 Java 程序。

> 堆就是堆,而不是树,我总是将堆跟树联系起来

## 基本数据类型

Java 中有 8 种基本数据类型，它们的大小如下：

1. byte（字节）：占用 8 位（1 字节），取值范围为 -128 到 127。
2. short（短整型）：占用 16 位（2 字节），取值范围为 -32,768 到 32,767。
3. int（整型）：占用 32 位（4 字节），取值范围为 -2,147,483,648 到 2,147,483,647。
4. long（长整型）：占用 64 位（8 字节），取值范围为 -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807。
5. float（单精度浮点型）：占用 32 位（4 字节），取值范围约为 -3.4e38 到 3.4e38，精度约为 7 位小数。
6. double（双精度浮点型）：占用 64 位（8 字节），取值范围约为 -1.8e308 到 1.8e308，精度约为 16 位小数。
7. char（字符型）：占用 16 位（2 字节），取值范围为 0 到 65,535，用于表示 Unicode 字符。
8. boolean（布尔型）：占用的位数在不同的 Java 虚拟机实现中可能不同，通常为 8 位（1 字节）或 32 位（4 字节），只有两个取值：true 和 false。

这些基本数据类型直接存储在栈内存中，它们不是对象，因此不需要通过引用访问。在 Java 中，基本数据类型的大小是固定的，不会因为操作系统或硬件平台的不同而发生变化。

## 内存泄漏的情况

在 Java 中，内存泄漏是指一些不再需要的对象占用的内存无法被**垃圾回收器回收，导致内存资源无法释放**。以下是一些可能导致内存泄漏的常见情况：

1. **长生命周期对象持有短生命周期对象的引用**：如果一个长生命周期的对象（例如静态变量、单例对象）持有一个短生命周期对象的引用，即使短生命周期对象不再使用，垃圾回收器也无法回收它，因为仍然存在对它的引用。

2. 集合类对象：集合类（如 ArrayList、HashMap 等）可能会导致内存泄漏，特别是在长生命周期对象中。如果不及时清理集合中不再使用的对象，它们会一直占用内存。

3. 监听器和回调：当一个对象注册为另一个对象的监听器或回调时，它可能会导致内存泄漏。如果在不再需要监听或回调时没有取消注册，这些对象将继续存在并占用内存。

4. 内部类和外部类之间的引用：非静态内部类会隐式持有一个对其外部类的引用。如果外部类的生命周期比内部类长，且内部类对象长时间存在，可能会导致内存泄漏。可以考虑将内部类更改为静态内部类以避免此问题。

5. 资源未关闭：在 Java 应用中，使用到的一些资源（如文件流、数据库连接等）需要在使用完毕后显式关闭。如果没有正确关闭这些资源，它们可能会导致内存泄漏。

6. 线程泄漏：线程本身也会占用内存资源，特别是线程的栈内存。如果线程没有正确终止，可能导致内存泄漏。线程池的不当使用也可能导致线程泄漏，因此要确保合理配置线程池，并在任务完成后正确释放线程。

要避免内存泄漏，需要密切关注程序中的对象引用、资源管理和线程管理等方面。在开发过程中，可以使用一些内存分析工具（如 VisualVM、MAT 等）来检测和分析内存泄漏。



java只会为**类的属性自动初始化(基本数据类型有其默认值,对象为空),而不会为局部变量进行初始化**,因此局部变量如果没有初始化,便会报错,这里是跟c++的区别,这种思想也合理吧,局部变量你不初始化说明你压根用不着,又何必定义,但是也不太合理,如果我是在一个条件里面初始化,那么外界又拿不到,外界初始化的话就得给一个值先冒充着

## 总结

本章的话大致讲了一些基础东西,比如栈,堆,类的基本定义啊,文档注释这些

# 第三章 控制程序流程

> 就象任何有感知的生物一样，程序必须能操纵自己的世界，在执行过程中作出判断与选择。

## 运算符

Java 中有许多运算符，可以根据功能和优先级分为以下类别：

1. 后缀运算符：
   - `expr++`：后缀递增
   - `expr--`：后缀递减

2. 一元运算符：
   - `++expr`：前缀递增
   - `--expr`：前缀递减
   - `+expr`：正号
   - `-expr`：负号
   - `!expr`：逻辑非（布尔取反）
   - `~expr`：按位非（按位取反）

3. 类型转换运算符：
   - `(type) expr`：类型转换（强制类型转换）

4. 算术运算符：
   - `*`：乘法
   - `/`：除法
   - `%`：取模（求余数）
   - `+`：加法
   - `-`：减法

5. 移位运算符：
   - `<<`：左移
   - `>>`：右移（带符号）
   - `>>>`：无符号右移

6. 关系运算符：
   - `<`：小于
   - `<=`：小于等于
   - `>`：大于
   - `>=`：大于等于
   - `instanceof`：类型检查

7. 相等运算符：
   - `==`：相等
   - `!=`：不等

8. 位运算符：
   - `&`：按位与
   - `^`：按位异或
   - `|`：按位或

9. 短路逻辑运算符：
   - `&&`：逻辑与（短路）
   - `||`：逻辑或（短路）

10. 条件运算符（三元运算符）：
    - `expr1 ? expr2 : expr3`：条件表达式

11. 赋值运算符：
    - `=`：赋值
    - `+=`：加法赋值
    - `-=`：减法赋值
    - `*=`：乘法赋值
    - `/=`：除法赋值
    - `%=`：取模赋值
    - `<<=`：左移赋值
    - `>>=`：右移赋值
    - `>>>=`：无符号右移赋值
    - `&=`：按位与赋值
    - `^=`：按位异或赋值
    - `|=`：按位或赋值

运算符优先级（从高到低）：

1. 后缀运算符
2. 一元运算符
3. 类型转换运算符
4. 算术运算符（`*`、`/`、`%` 优先于 `+`、`-`）
5. 移位运算符
6. 关系运算符
7. 相等运算符
8. 位运算符（`&` 优先于 `^`,^` 优先于 `|)
9. `短路逻辑运算符（`&&` 优先于 `||`）
10. 条件运算符（三元运算符）
11. 赋值运算符

请注意，在表达式中使用多个运算符时，优先级相同的运算符将根据其结合性从左到右（或从右到左）进行求值。大多数运算符（如算术、关系、位运算等）具有从左到右的结合性，而一元运算符、赋值运算符和条件运算符则具有从右到左的结合性。

为了提高代码的可读性和可维护性，建议使用括号明确地指定运算符的优先级，而不是仅依赖于运算符的默认优先级。这可以帮助避免因误解优先级而导致的错误。



## java 为什么没有sizeof ?

因为他不需要,c++和c有sizeof 是因为在不同的平台里面,有些数据类型的大小是不一样的,new 数据的时候就得通过sizeof去控制

## 流程控制

Java 中的流程控制结构可以分为三大类：顺序结构、分支结构和循环结构

### 顺序结构

顺序结构中的代码会按照它们在源文件中的顺序自上而下执行。

```java
statement1;
statement2;
statement3;
...
```

### 分支结构

#### if 语句

```java
if (condition) {
    // 当条件为真时执行的代码块
}
```

- if-else 语句

```java
if (condition) {
    // 当条件为真时执行的代码块
} else {
    // 当条件为假时执行的代码块
}
```

- if-else if-else 语句

```java
if (condition1) {
    // 当条件1为真时执行的代码块
} else if (condition2) {
    // 当条件1为假，且条件2为真时执行的代码块
} else {
    // 当所有条件均为假时执行的代码块
}
```

#### switch 语句

```java
switch (expression) {
    case value1:
        // 当 expression 等于 value1 时执行的代码块
        break;
    case value2:
        // 当 expression 等于 value2 时执行的代码块
        break;
    ...
    default:
        // 当 expression 与所有 case 值都不匹配时执行的代码块
}
```

- `expression`：用于与 `case` 语句中的值进行比较的表达式。在 Java 7 之前，该表达式只能是整型（byte、short、char、int）或枚举类型；从 Java 7 开始，还可以是字符串类型。
- `case`：定义了一个与 `expression` 进行比较的值,这个值必须与expression的返回值类型相同。如果 `expression` 等于 `case` 后的值，那么将执行该 `case` 语句下的代码块。
- `break`：用于跳出 `switch` 语句。如果不使用 `break`，则代码将继续执行下一个 `case` 语句，直到遇到 `break` 或 `switch` 结构结束。
- `default`：当 `expression` 与所有 `case` 值都不匹配时执行的代码块。`default` 语句是可选的，可以省略。

注意点

1. 唯一的 case 值：确保每个 `case` 语句的值都是唯一的，以避免产生歧义。具有相同值的多个 `case` 语句会导致编译错误。

### 循环结构

- for 循环

```java
for (initialization; condition; update) {
    // 当条件为真时执行的代码块，每次迭代后执行更新操作
}
```

- while 循环

```java
while (condition) {
    // 当条件为真时执行的代码块
}
```

- do-while 循环

```java
do {
    // 代码块至少执行一次，然后在条件为真时继续执行
} while (condition);
```

请注意，这些格式只是通用模板。在实际编程中，您可能需要根据具体需求对这些结构进行适当的修改。同时，为了提高代码的可读性，建议在复杂的逻辑中使用括号和适当的缩进。

> 对于condition,必须是bool表达式



## 总结

本小结主要讲述了java中的运算符,计算,类型转换,还有流程控制,中规中矩

# 第四章 初始化与清除



## 初始化

### 类的初始化

类的初始化是指在类首次加载到 JVM（Java 虚拟机）时执行的过程。类的初始化主要包括静态变量的赋值和静态代码块的执行。这些操作仅在类加载时执行一次。类初始化如下：

- 静态变量赋值：按照它们在类中出现的顺序为静态变量分配内存并赋初值。
- 静态代码块执行：按照它们在类中出现的顺序执行静态代码块。

> 会按照static关键字的定义顺序来依次执行,静态变量和静态代码块的初始化顺序取决于它们在类中的出现顺序。为了避免在静态代码块中访问尚未初始化的静态变量，确保在静态代码块之前对静态变量进行初始化。

### 对象初始化

 对象的初始化是指创建对象实例并为实例变量分配内存和初始值的过程。对象初始化如下：

- 分配内存：为对象分配内存空间。
- 实例变量赋值：按照它们在类中出现的顺序为实例变量分配内存并赋初值。
- 实例初始化块执行：按照它们在类中出现的顺序执行实例初始化块。
- 构造函数执行：调用相应的构造函数以进一步初始化对象。

> 同理,实例变量和实例代码块的初始化顺序取决于它们在类中的出现顺序

综上所述，类的初始化和对象的初始化是 Java 中创建和使用对象的两个关键步骤。类的初始化负责静态变量的赋值和静态代码块的执行，而对象的初始化则涉及实例变量的赋值、实例初始化块的执行和构造函数的调用。类的初始化只在类加载时执行一次，而对象的初始化在每次创建新对象时执行。

## 资源问题

如果程序结束了,那么它占用的资源都会归还给操作系统,比如你打开一个文件流,忘记关闭了,程序结束后,还是会归回给操作系统,不过这样并不是一个好习惯,如果我们的程序是要一直执行的,那么这样会浪费系统资源., 但是即使是一次执行的程序,不关闭文件也会存在一些潜在问题:

1. 文件锁定：在程序运行期间，如果文件没有被正确关闭，其他程序可能无法访问或修改该文件。这可能导致数据不一致或协同工作问题。

2. 程序行为不稳定：当打开的文件数量达到系统允许的最大值时，操作系统可能会拒绝打开新文件。这可能导致程序行为不稳定，甚至崩溃。

3. 不良编程习惯：不养成正确关闭资源的习惯可能导致在其他项目或长时间运行的程序中出现问题。遵循最佳实践，始终确保在使用完资源后正确关闭它们。

因此，尽管在一次性执行的程序中，未关闭的文件流可能不会导致长期问题，但仍然建议采用诸如 try-with-resources 语句等方法来确保文件流在使用完毕后被正确关闭。这有助于避免潜在问题，提高代码质量和可维护性。

## 总结

这章主要讲了一些类的初始化,垃圾回收器,方法重载的东西

# 第五章 隐藏实施过程

* **进行面向对象的设计时，一项基本的考虑是：如何将发生变化的东西与保持不变的东西分隔开**

* **创建自己的包时，要求 package 语句必须是文件中的第一个“非注释”代码**

* **编译器遇到 import 语句后，它会搜索由CLASSPATH 指定的目录,然后查找名称适当的已编译文件(.class文件)**
* **为导入的类首次创建一个对象时（或者访问一个类的static 成员时）**，编译器会在适当的目录里寻找同名的.class 文件（所以如果创建类 X 的一个对象，就应该是 X.class）。若只发现X.class，它就是必须使用的那一个类。然而，如果它在相同的目录中还发现了一个 X.java，编译器就会比较两个文件的日期标记。如果X.java 比X.class 新，**就会自动编译 X.java，生成一个最新的 X.class。**

## 访问修饰符

Java 中有四种访问修饰符，用于限制类、方法、变量和内部类的可见性和访问范围。它们是：public, private, protected 和默认（即不使用任何修饰符，有时也称为“包私有”或“默认访问”）。

1. public：
   - 描述：被 public 修饰的**类、方法或变量**可以在任何地方被访问。
   - 类：public 类可以被任何其他类访问。
   - 方法和变量：public 方法和变量可以被该类的所有对象和任何其他类访问。
   - 内部类：public 内部类可以在任何地方被访问。

2. private：
   - 描述：被 private 修饰的**方法或变量**只能在声明它们的类中被访问。
   - 类：**private 不能修饰顶级类，但可以修饰内部类**。
   - 方法和变量：private 方法和变量只能在声明它们的类中被访问，不能在该类的子类或其他类中访问。
   - 内部类：private 内部类只能在声明它的类中被访问。

3. protected：
   - 描述：被 protected 修饰的方法或变量可以在声明它们的类中、该类的子类以及同一包中的其他类中被访问。
   - 类：**protected 不能修饰顶级类，但可以修饰内部类。**
   - 方法和变量：protected 方法和变量可以在声明它们的类中、该类的子类以及同一包中的其他类中被访问。
   - 内部类：protected 内部类可以在声明它的类中、该类的子类以及同一包中的其他类中被访问。

4. 默认（包私有）：
   - 描述：不使用任何访问修饰符的**类、方法或变量**只能在同一包中被访问。
   - 类：默认访问的类只能在同一包中的其他类访问。
   - 方法和变量：默认访问的方法和变量可以在声明它们的类中以及同一包中的其他类中被访问。
   - 内部类：**默认访问的内部类可以在声明它的类中以及同一包中的其他类中被访问**。

总结：
- public：最开放的访问级别，可以在任何地方被访问。
- private：最严格的访问级别，只能在声明它的类中访问。
- protected：可以在声明它的类中、该类的子类以及同一包中的其他类中访问。
- 默认（包私有）：只能在同一包中的类访问。

> private > 默认 > protected > public

选择适当的访问修饰符有助于保护数据和保护数据和实现封装。通过限制对类、方法和变量的访问，可以确保它们的正确使用，并防止意外修改或错误的操作。

在实际编程中，通常遵循以下原则：

1. 最小权限原则：总是尽量使用最严格的访问修饰符。这有助于保护数据和实现封装，确保类的内部实现不会被外部错误地访问或修改。例如，如果一个变量只在类内部使用，那么将其声明为 private。

2. 面向接口编程：对外暴露接口，隐藏实现细节。通过使用 public 访问修饰符为类提供公共接口，**同时将内部实现细节封装在 private 和 protected 成员中**。

3. 适当使用包和模块：通过将相关的类组织在同一个包或模块中，可以使用默认（包私有）访问修饰符来限制它们的可见性范围。这可以使代码结构更加清晰，并减少错误的可能性。

4. 保护继承：对于需要子类访问的成员，可以使用 protected 访问修饰符。这允许子类访问和重写这些成员，同时仍然限制其他类的访问。

总之，合理地使用访问修饰符有助于保护数据和实现封装，确保类的正确使用和扩展。要充分理解每种访问修饰符的特点，并在实际编程中灵活运用。

> 

## 总结

本章主要讲了包和访问修饰符(public protected default private)



# 第六章 类的派生



## 继承

好的，让我们详细了解一下Java中的类继承。

1. 继承的概念
   继承是面向对象编程中的一个核心概念，它允许一个类从另一个类继承属性和方法。继承的主要目的是实现代码的复用和扩展。在Java中，继承使用关键字 `extends` 表示。

2. 基类（父类）与子类
   - 父类（也称为基类或超类）：被其他类继承的类。父类包含的属性和方法可以被子类继承。
   - 子类：从父类继承属性和方法的类。子类可以扩展和修改从父类继承的属性和方法。

3. 继承的语法
   子类使用关键字 `extends` 继承父类。例如：
   ```java
   class Parent {
       // 父类的属性和方法
   }
   
   class Child extends Parent {
       // 子类的属性和方法
   }
   ```

4. 访问控制与继承
   - **private成员（属性和方法）不能被子类直接访问。**
   - **默认访问权限（没有访问修饰符）的成员可以被同一个包中的子类访问。**
   - protected成员可以被同一个包中的子类以及不同包中的子类访问。
   - public成员可以被任何地方的子类访问。

5. 方法重写（覆盖）
   子类可以重写从父类继承的方法，以提供新的实现。重写方法的要求：
   - 方法名、参数列表和返回类型必须与父类方法相同。
   - 访问修饰符不能比父类方法更严格。
   - 重写方法不能抛出比父类方法更多的受检异常。

6. super关键字
   子类可以使用super关键字引用父类的成员（属性和方法）。
   - super调用父类的构造方法：`super()` 必须是子类构造方法中的第一个语句。
   - super访问父类的属性：`super.attribute`
   - super调用父类的方法：`super.method()`

7. final关键字与继承
   - 如果一个类用final修饰，那么它不能被继承。例如：`final class A {}`
   - 如果一个方法用final修饰，那么它不能被子类重写。例如：`final void method() {}`
   - 如果一个变量被final修饰,那么它不能被修改这里的修改指的是修改它对应的地址值

8. 抽象类与抽象方法
   - 抽象类：使用关键字 `abstract` 定义的类，不能被实例化。抽象类可以包含抽象方法和具体方法。
   - 抽象方法：使用关键字 `abstract` 定义的方法，没有方法体。抽象方法必须在抽象类中定义，子类需要提供实现。

   ```java
   abstract class Animal {
       abstract void sound(); // 抽象方法，没有方法体
       
       void move() {
           // 具体方法
           System.out.println("Animal is moving");
       }
   }
   
   class Dog extends Animal {
       // 子类必须实现抽象方法
       void sound() {
           System.out.println("Dog barks");
       }
   }
   
   ```

   

9. 接口与继承 接口是Java中的一种特殊类型，它包含了一组**抽象方法（Java 8引入了默认方法和静态方法）**。实现接口的类必须提供接口中所有方法的实现。一个类可以实现多个接口，使用关键字 `implements`。

   语法示例：

   ```java
   csharpCopy codeinterface Flyable {
       void fly();
   }
   
   interface Swimmable {
       void swim();
   }
   
   class Bird implements Flyable, Swimmable {
       // 实现接口中的方法
       void fly() {
           System.out.println("Bird flies");
       }
   
       void swim() {
           System.out.println("Bird swims");
       }
   }
   ```

10. 多重继承与接口 **Java不支持多重继承**（一个类继承多个类），但可以通过实现多个接口来实现多重继承的效果。一个类可以同时实现多个接口，从而继承接口中的方法。

11. 构造器与继承 子类构造方法默认调用父类的无参构造方法。如果父类没有提供无参构造方法，那么子类必须使用super关键字显式调用父类的构造方法。**(必须是方法体的第一条语句)**

    语法示例：

    ```java
    javaCopy codeclass Parent {
        Parent(int a) {
            // 父类的构造方法
        }
    }
    
    class Child extends Parent {
        Child(int a) {
            super(a); // 显式调用父类的构造方法
        }
    }
    ```

### 属性冲突

在 Java 继承和接口实现中，属性冲突主要包括以下两种情况：

1. 类继承中的属性冲突：

   当子类和父类中具有相同名称的属性时，子类中的属性会遮蔽父类中具有相同名称的属性。也就是说，当在子类中访问该属性时，将访问子类中的属性，而不是父类中的属性。但是可以通过 `super` 关键字显式地访问父类中的属性。例如：

   ```
   class Parent {
       String name = "Parent";
   }

   class Child extends Parent {
       String name = "Child";

       void printNames() {
           System.out.println(name);         // 输出 "Child"
           System.out.println(super.name);    // 输出 "Parent"
       }
   }
   ```

2. 接口实现中的属性冲突：

   接口可以定义属性（默认为 `public static final`），当一个类实现多个接口，且这些接口具有相同名称的属性时，可能会出现冲突。在这种情况下，实现类需要显式指定访问哪个接口的属性，否则会出现编译错误。例如：

   ```java
   interface InterfaceA {
       String name = "InterfaceA";
   }
   
   interface InterfaceB {
       String name = "InterfaceB";
   }
   
   class Implementor implements InterfaceA, InterfaceB {
       void printNames() {
           System.out.println(InterfaceA.name); // 输出 "InterfaceA"
           System.out.println(InterfaceB.name); // 输出 "InterfaceB"
           //System.out.println(name);         // 编译错误，因为不明确是访问 InterfaceA 还是 InterfaceB 的属性
       }
   }
   ```

综上所述，要避免属性冲突，最佳实践是：

- 尽量避免在子类和父类、接口之间使用相同名称的属性。
- 如果确实需要访问父类或接口中的同名属性，可以使用 `super` 关键字（对于父类属性）或显式指定接口名称（对于接口属性）进行访问。

> 如果父类和接口属性冲突了的话,那么父类属性变量优先,如果遇到了冲突想要使用父类或者接口中的值的话,得指定类名或者接口名字,而且必须在类中才能这样,比如在某个方法里面使用 super.变量 或者 接口名字.变量

## 总结

本章主要讲了继承的相关知识点,以及final的用法

# 第七章 多态性



## 抽象类

抽象类（Abstract Class）是 Java 中一个重要的面向对象编程概念。它是一种特殊的类，主要用于表示一组相关对象的共同特征。抽象类**不能直接实例化，需要通过继承来创建具体的子类实例**。以下是关于 Java 抽象类的一些关键知识点：

1. 抽象类的定义：使用 `abstract` 关键字来定义抽象类。例如：

   ```java
   abstract class Animal {
       // 类的内容
   }
   ```

2. 抽象方法：抽象类中可以包含抽象方法，也可以包含具体的方法。抽象方法没有方法体，只有方法签名，使用 `abstract` 关键字定义。子类必须实现抽象方法，否则子类也需要被声明为抽象类。例如：

   ```java
   abstract class Animal {
       abstract void makeSound(); // 抽象方法
       
       void breathe() {
           // 具体方法实现
       }
   }
   ```

3. 继承抽象类：当一个类继承了抽象类，它需要实现抽象类中的所有抽象方法。例如：

   ```java
   class Dog extends Animal {
       void makeSound() {
           System.out.println("Dog barks");
       }
   }
   ```

4. 实例化子类：抽象类不能直接实例化，但可以通过实例化其子类来创建对象。例如：

   ```java
   Animal myDog = new Dog(); // 创建 Dog 类的实例
   myDog.makeSound();        // 调用子类实现的抽象方法
   myDog.breathe();          // 调用抽象类中的具体方法
   ```

5. 抽象类的目的：抽象类的主要目的是为了提供一个公共接口和基本实现，以便其他类可以从抽象类继承并**共享相同的方法和属性**。这有助于实现代码复用和多态。

6. 抽象类与接口：抽象类和接口都是用于定义对象的共同特征和行为。但是，**抽象类可以包含具体方法和属性**，而**接口只能包含抽象方法和常量**。此外，一个类可以实现多个接口，但只能继承一个抽象类。

这些是 Java 抽象类的主要知识点。在实际编程过程中，了解抽象类的概念和用法对于实现高质量、可维护的面向对象程序非常重要。



## 接口

接口（Interface）是 Java 中另一个重要的面向对象编程概念。接口定义了一组方法的签名，规定了实现接口的类必须具备哪些行为。接口不能直接实例化，需要通过实现接口的类来创建具体对象。以下是关于 Java 接口的一些关键知识点：

1. 接口的定义：使用 `interface` 关键字来定义接口。例如：

   ```java
   interface Drawable {
       // 接口的内容
   }
   ```

2. 接口方法：在 Java 8 之前，接口中只能包含抽象方法（方法签名，没有方法体）。从 Java 8 开始，接口中**可以包含默认方法（具有默认实现的方法）和静态方法**。例如：

   ```java
   interface Drawable {
       void draw(); // 抽象方法

       default void setColor(String color) {
           // 默认方法实现
       }

       static void printInfo() {
           // 静态方法实现
       }
   }
   ```

3. 实现接口：一个类可以通过 `implements` 关键字来实现一个或多个接口。实现接口的类必须实现接口中的所有抽象方法（除非它是抽象类）。例如：

   ```java
   class Circle implements Drawable {
       void draw() {
           System.out.println("Drawing a circle");
       }
   }
   ```

4. 多接口实现：一个类可以实现多个接口。在这种情况下，类必须实现所有接口中的抽象方法。例如：

   ```java
   class Circle implements Drawable, Resizable {
       // 实现 Drawable 接口的方法
       void draw() {
           System.out.println("Drawing a circle");
       }
       
       // 实现 Resizable 接口的方法
       void resize(double factor) {
           // 方法实现
       }
   }
   ```

5. 接口继承：接口可以通过 `extends` 关键字继承其他接口。继承接口的接口将包含所有父接口的抽象方法。例如：

   ```java
   interface MovableDrawable extends Drawable {
       void move(int x, int y);
   }
   ```

6. 接口的目的：**接口的主要目的是为了提供一种约定，规定实现接口的类应该具备哪些行为。这有助于实现多态和提高代码的可维护性。**

7. 接口与抽象类的区别：接口和抽象类都是用于定义对象的共同特征和行为。但是，抽象类可以包含具体方法和属性，而接口只能包含抽象方法和常量。此外，一个类可以实现多个接口，但只能继承一个抽象类。

这些是 Java 接口的主要知识点。了解接口的概念和用法对于实现高质量、可维护的面向对象程序非常重要。

## 多态

Java 中的多态是面向对象编程的一个核心特性，它允许在运行时根据对象的实际类型来执行特定的实现，而非仅根据引用类型。多态实现了代码的灵活性和可扩展性，使得我们可以编写更加通用且易于维护的代码。

多态的主要特点如下：

1. 继承：多态的基础是继承。子类继承父类，从而可以拥有父类的属性和方法。这为多态提供了基本的条件。

2. 方法重写（Override）：子类可以重写父类的方法，以提供自己的实现。**当我们使用子类对象调用该方法时，将执行子类的实现，而非父类的实现。**

3. 向上转型（Upcasting）：**子类的对象可以隐式地转换为父类类型。这意味着我们可以使用父类类型的引用来指向子类的对象**。向上转型在运行时不会**丢失对象的类型信息**。

4. 动态方法分派：**多态的核心在于在运行时根据对象的实际类型动态地决定调用哪个方法实现。也就是说，当我们使用父类类型的引用调用一个被子类重写的方法时，Java 虚拟机会在运行时确定执行的具体方法。**

这里有一个多态的例子：

```java
// 父类
class Animal {
    void speak() {
        System.out.println("The animal speaks.");
    }
}

// 子类 1
class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("The dog barks.");
    }
}

// 子类 2
class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("The cat meows.");
    }
}

public class Main {
    public static void main(String[] args) {
        // 向上转型
        Animal myAnimal = new Dog();
        myAnimal.speak(); // 输出：The dog barks.

        myAnimal = new Cat();
        myAnimal.speak(); // 输出：The cat meows.

        // 直接使用父类类型的引用
        makeAnimalSpeak(new Dog()); // 输出：The dog barks.
        makeAnimalSpeak(new Cat()); // 输出：The cat meows.
    }

    // 多态的方法
    public static void makeAnimalSpeak(Animal animal) {
        animal.speak();
    }
}
```

在这个例子中，`Dog` 和 `Cat` 类都继承自 `Animal` 类并重写了 `speak` 方法。我们可以看到，当我们使用 `Animal` 类型的引用调用 `speak` 方法时，实际执行的方法取决于对象的实际类型。这就是多态的体现。

总之，Java 中的多态允许我们编写更加灵活且易于维护的代码。多态主要涉及到继承、方法重写、向上转型、动态方法分配.

### 多态的优点

多态在 Java 和其他面向对象编程语言中具有很多优势，以下是一些主要优势：

1. 代码重用：多态允许子类继承父类的属性和方法，从而减少了代码的重复。同时，子类可以根据需求重写或扩展父类的方法，使得代码更加灵活。

2. 解耦：多态可以降低代码之间的耦合度。当我们编写一个方法时，**只需要关注该方法所需的接口或父类，而不必关心具体的实现类**。这使得我们可以在不修改方法的情况下，替换或扩展实现类。

3. 提高可扩展性：多态使得我们可以轻松地扩展程序的功能。例如，**我们可以添加新的子类来扩展程序的功能，而不需要修改已有的代码**。

4. 提高代码的可维护性：由于多态降低了代码之间的耦合度，使得代码结构更加清晰，这有助于提高代码的可维护性。

5. 接口抽象：**多态允许我们将接口与实现分离，使得我们可以专注于设计接口，而不必关心具体的实现**。这有助于提高代码的可读性和可维护性。

6. 更灵活的代码组织：通过多态，我们可以使用父类或接口类型的引用来引用子类的对象。这使得我们可以在运行时动态地决定使用哪个对象，从而实现更加灵活的代码组织。

总之，多态是面向对象编程的一个核心特性，它为我们提供了代码重用、解耦、可扩展性、可维护性等诸多优势。通过掌握多态，我们可以编写更加优雅、灵活且易于维护的代码。

## 内部类

### 定义

Java 中的内部类是指在一个类的内部定义的类。内部类主要用于**组织和封装代码**，使代码结构更加清晰。根据其声明位置和特点，内部类可以分为以下四种类型：

1. 成员内部类（Member Inner Class）：
   - 成员内部类是在一个类的内部声明的**非静态类**。
   - **成员内部类可以访问外部类的所有成员（包括私有成员）**。
   - **要创建成员内部类的实例，需要先创建外部类的实例**。
   - **成员内部类不能包含静态成员（除非是编译时常量）。**
   - 成员内部类可以使用外部类的访问修饰符（public, private, protected, 默认）。

2. 静态内部类（Static Inner Class）：
   - 静态内部类是在一个类的内部声明的静态类。
   - **静态内部类可以访问外部类的静态成员（包括私有静态成员），但不能访问外部类的非静态成员。**
   - 创建静态内部类的实例**不需要先创建外部类的实例。**
   - 静态内部类可以包含静态成员和非静态成员。
   - 静态内部类可以使用外部类的访问修饰符（public, private, protected, 默认）。

3. 局部内部类（Local Inner Class）：
   - **局部内部类是在一个方法或代码块内部声明的类。**
   - 局部内部类只能访问所在方法中被声明为 final 或者是 effectively final 的局部变量（从 Java 8 开始）。
   - 局部内部类不能使用访问修饰符，其可见性仅限于声明它的方法或代码块。
   - 局部内部类不能包含静态成员（除非是编译时常量）。
   - 创建局部内部类的实例需要在其所在方法或代码块内部进行。

4. 匿名内部类（Anonymous Inner Class）：
   - 匿名内部类是一种没有类名的内部类，通常用于创建临时的类实例。
   - 匿名内部类可以继承一个类或实现一个接口，但不能同时继承多个类或接口。
   - **匿名内部类只能访问所在方法中被声明为 final 或者是 effectively final 的局部变量（从 Java 8 开始）**。
   - 匿名内部类不能包含静态成员（除非是编译时常量）。
   - 创建匿名内部类的实例需要在其所在方法或代码块内部进行，通常通过 new 操作符实现。

总结：内部类是 Java **提供的一种强大的代码组织和封装机制**。了解不同类型的内部类及其特点，可以帮助您在实际编程中更加灵活地运用内部类来实现代码的封装和模块化。以下是一些内部类的典型用途和注意事项：

1. 封装：内部类可以访问外部类的成员，这使得它们成为实现封装的理想选择。通过将与外部类密切相关的功能实现在内部类中，可以使外部类更加简洁，更易于理解和维护。

2. 实现回调和事件处理：匿名内部类通常用于实现回调和事件处理，因为它们可以直接访问所在方法的局部变量和外部类的成员。这在实现图形用户界面（GUI）等事件驱动程序时特别有用。

3. 实现多重继承：虽然 Java 不支持多重继承，但可以通过使用内部类来实现类似的功能。外部类可以包含多个内部类，每个内部类分别继承或实现不同的类或接口。

4. 静态内部类和单例模式：静态内部类可以用于实现单例模式，因为它们不依赖于外部类的实例。这可以确保类在整个应用程序中只有一个实例，从而节省资源并提高性能。

注意事项：

1. 避免内部类和外部类之间的过度耦合。虽然内部类可以访问外部类的成员，但过度使用这种关系可能导致代码难以理解和维护。尽量让内部类和外部类之间的关系清晰，遵循单一职责原则。

2. 谨慎使用匿名内部类。匿名内部类在某些场景下非常有用，但它们的可读性较差。在需要实现复杂逻辑的情况下，考虑使用具名的内部类或外部类。

3. 考虑性能影响。成员内部类、局部内部类和匿名内部类都需要隐式地持有对外部类实例的引用。这可能导致内存泄漏和性能问题。在这种情况下，可以考虑使用静态内部类，因为它们不持有对外部类实例的引用。

通过了解和掌握内部类的特点和用法，您可以更有效地利用 Java 语言的特性，编写出更加清晰、易于维护的代码。

### 使用例子

以下是几种内部类的示例，包括正确和错误的用法。

1. 成员内部类：

正确用法：

```java
class Outer {
    private String message = "Hello, Inner!";

    class Inner {
        void printMessage() {
            System.out.println(message); // 访问外部类的成员变量
        }
    }

    public static void main(String[] args) {
        Outer outer = new Outer();
        Outer.Inner inner = outer.new Inner(); // 创建内部类实例
        inner.printMessage();
    }
}
```

错误用法：

```java
class Outer {
    private String message = "Hello, Inner!";

    class Inner {
        static String staticMessage = "Static message"; // 成员内部类不能有静态变量
    }
}
```

2. 静态内部类：

正确用法：

```java
class Outer {
    static String message = "Hello, Static Inner!";

    static class StaticInner {
        void printMessage() {
            System.out.println(message); // 访问外部类的静态成员变量
        }
    }

    public static void main(String[] args) {
        Outer.StaticInner inner = new Outer.StaticInner(); // 创建静态内部类实例
        inner.printMessage();
    }
}
```

错误用法：

```java
class Outer {
    private String message = "Hello, Static Inner!";

    static class StaticInner {
        void printMessage() {
            System.out.println(message); // 静态内部类不能访问外部类的非静态成员变量
        }
    }
}
```

3. 局部内部类：

正确用法：

```java
class Outer {
    void createLocalInner() {
        final String message = "Hello, Local Inner!";

        class LocalInner {
            void printMessage() {
                System.out.println(message); // 访问所在方法的局部变量（必须是 final 或 effectively final）
            }
        }

        LocalInner localInner = new LocalInner();
        localInner.printMessage();
    }

    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.createLocalInner();
    }
}
```

错误用法：

```java
class Outer {
    void createLocalInner() {
        String message = "Hello, Local Inner!";

        class LocalInner {
            void changeMessage() {
                message = "New message"; // 局部内部类不能修改所在方法的局部变量
            }
        }
    }
}
```

4. 匿名内部类：

正确用法：

```java
interface Printer {
    void printMessage(String message);
}

class Outer {
    void createAnonymousInner() {
        Printer printer = new Printer() {
            @Override
            public void printMessage(String message) {
                System.out.println(message);
            }
        };

        printer.printMessage("Hello, Anonymous Inner!");
    }

    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.createAnonymousInner();
    }
}
```

错误用法：

```java
interface Printer {
    void printMessage(String message);
}

class Outer {
    void createAnonymousInner() {
        String message = "Hello, Anonymous Inner!";
        Printer printer = new Printer() {
            @Override
            public void printMessage(String newMessage) {
                message = newMessage; // 匿名内部类不能修改所在方法的局部变量（除非变量是 final 或 effectively final
            }
        }
    }

    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.createAnonymousInner();
    }
}

```

> 上述列子是在jdk8中使用的,其实在jdk15以后,就有些区别了,比如成员内部类允许有静态变量,局部内部类和匿名内部类可以访问非final变量

### 内部类的用处

内部类在 Java 编程中有很多用途，主要包括以下几点：

1. **封装**：内部类可以帮助将类的实现细节隐藏起来，使得外部类更简洁。它使得与外部类关系紧密的类能够被组织在一起，而不需要暴露给外部其他类。
2. **增强可读性和维护性**：将与某个类紧密相关的辅助类或逻辑组织在一起，可以提高代码的可读性和维护性。这样，相关代码可以在一个地方进行修改和维护，而不是分散在多个地方。
3. **访问外部类成员**：非静态内部类可以访问外部类的所有成员（包括私有成员），而无需显式传递引用。这使得编写能够访问外部类成员的方法更简单和高效。
4. **实现多重继承**：Java 不支持多重继承，但可以通过内部类实现一种形式的多重继承。你可以创建一个内部类，使其继承自另一个类，这样外部类就可以间接地继承内部类的父类。
5. **用于回调和事件处理**：内部类常用于回调和事件处理。例如，在图形用户界面（GUI）编程中，匿名内部类通常用于实现事件监听器。这样可以将事件处理逻辑与其他代码分离，提高代码的组织和可读性。

我们来看一段代码吧

```
import java.util.ArrayList;
import java.util.Iterator;

public class MyList implements Iterable<Integer> {

    private final int[] array = {1,2,3,4,5};

    class MyIterator implements java.util.Iterator<Integer>{
        private int index = 0;

        @Override
        public boolean hasNext() {
            return index < array.length;
        }

        @Override
        public Integer next() {
            return array[index++];
        }

    }

    public Iterator<Integer> iterator() {
        return new MyIterator();
    }

    public static void main(String[] args) {
        MyList myList = new MyList();
        ArrayList<Integer> integers = new ArrayList<>();
        for (Integer integer : myList) {
            System.out.println(integer);
        }
    }

}

```

这里我们自己定义了一个迭代器,这个迭代器就能很方便的访问数据,如果我们不使用内部类的的话,我们需要迭代器显示持有我们的对象,这样是比较麻烦的

## 总结

本章主要讲述了抽象类,接口,还有多态的相关概念,内部类(静态内部类 成员内部类 局部内部类 匿名内部类), 内部类这里在不同版本有不同的表现,在jdk16开始就有了一些变化

> 多态是针对方法的,而不是属性

# 第九章 异常

## Error

在 Java 中，`Error` 是一个继承自 `Throwable` 类的子类，表示程序运行过程中可能遇到的严重问题。**这些问题通常与 JVM（Java 虚拟机）或系统相关，如内存溢出、虚拟机错误、类加载错误等。`Error` 表示的问题通常是无法预期或无法恢复的，程序员通常无法处理这些错误。**

`Error` 的作用是在程序运行时提供一种表示严重问题的机制，以便于开发者了解发生的问题并进行调试。当一个 `Error` 发生时，程序通常会终止执行，因为这些错误通常意味着程序无法继续运行。然而，在实际开发过程中，程序员通常不需要处理 `Error`，因为这些错误往往是无法恢复的。

一些常见的 `Error` 子类包括：

- `OutOfMemoryError`：表示 JVM 中没有足够的内存来分配对象。
- `StackOverflowError`：表示线程的栈空间已满，无法继续执行。
- `LinkageError`：表示类的加载或链接过程中发生错误，例如 `NoClassDefFoundError` 或 `ClassNotFoundException`。
- `VirtualMachineError`：表示 JVM 发生内部错误，例如 `InternalError` 或 `UnknownError`。

尽管 `Error` 及其子类表示程序中的严重问题，但请注意，这些类并不是用于表示程序逻辑错误或可预期的异常情况。对于这些情况，应使用 `Exception` 类及其子类。



## Exception

Java 异常是程序执行过程中发生的错误或异常情况。Java 提供了一套异常处理机制，帮助程序员在出现异常时捕获和处理它们，以保证程序的正常运行。以下是 Java 异常的一些关键知识点：

1. 异常分类：Java 异常主要分为两类：**受检异常（Checked Exceptions）**和**非受检异常（Unchecked Exceptions）**。受检异常继承自 `java.lang.Exception` 类，需要显式处理（捕获或声明抛出）。**非受检异常继承自 `java.lang.RuntimeException` 类，不强制处理，可以选择性捕获。**

2. 常见的异常类：
   - 受检异常：`IOException`（输入输出异常）、`FileNotFoundException`（找不到文件异常）、`ClassNotFoundException`（找不到类异常）等。
   - 非受检异常：`NullPointerException`（空指针异常）、`IndexOutOfBoundsException`（数组越界异常）、`ArithmeticException`（算术异常，如除以零）等。

3. 异常处理：Java 使用 `try-catch` 语句块来捕获和处理异常。`try` 块包含可能抛出异常的代码，`catch` 块用于捕获特定类型的异常并处理。例如：

```java
try {
    // 可能抛出异常的代码
} catch (ExceptionType1 e) {
    // 处理 ExceptionType1 的代码
} catch (ExceptionType2 e) {
    // 处理 ExceptionType2 的代码
}
```

4. `finally` 块：`finally` 块是一个可选的代码块，它在 `try-catch` 语句块之后执行。无论 `try` 块中是否发生异常，`finally` 块的代码都会执行。通常用于关闭资源，如文件、数据库连接等。

```java
try {
    // 可能抛出异常的代码
} catch (ExceptionType e) {
    // 处理异常的代码
} finally {
    // 总是执行的代码
}
```

5. **异常传播**：当方法内部发生异常，且未在方法内部处理时，异常会传播到调用方法的地方。如果调用方法也没有处理异常，异常会继续传播，直到被捕获或导致程序终止。可以使用 `throws` 关键字声明方法可能抛出的异常类型，将异常传播给调用者处理。例如：

```java
public void readFile(String fileName) throws FileNotFoundException {
    // 可能抛出 FileNotFoundException 的代码
}
```

6. 自定义异常：可以通过继承 `Exception` 类或其子类来创建自定义异常。自定义异常可以为特定问题提供更具体的信息。例如：

```java
class CustomException extends Exception {
    public CustomException(String message) {
        super(message);
    }
}
```

易错点：

1. 不要捕获所有异常：尽量避免使用 `catch (Exception e)` 来捕获所有类型的异常，因为这样会使得代码难以维护和调试。应该尽量捕获和处理具体的异常类型，以便更好地了解和处理问题。
2. 不要忽略异常：捕获异常后，应该对异常进行处理，例如记录日志、通知用户或尝试恢复。不要只是简单地捕获异常而不进行处理，这样可能会掩盖潜在的问题。
3. 适当地处理异常：在捕获异常时，应尽量采取适当的措施来处理异常。例如，可以关闭资源、释放内存、进行回滚操作等。此外，需要确保资源在出现异常时能够正确关闭，可以在 `finally` 块中执行这些操作。
4. **优先使用非受检异常**：在自定义异常时，如果异常是由编程错误导致的（例如空指针、数组越界等），优先使用非受检异常。如果异常是由外部因素导致的（例如 I/O 错误、网络问题等），则使用受检异常。
5. 不要过度使用异常：异常处理会导致程序运行效率降低，因此应该谨慎使用。在可以避免使用异常的情况下，尽量使用其他方式来处理错误。
6. 使用异常链：当捕获到一个异常，并需要抛出另一个异常时，可以使用异常链将原始异常作为新异常的一个属性，从而保留原始异常的信息。例如：

```java
try {
    // 可能抛出 IOException 的代码
} catch (IOException e) {
    throw new CustomException("Failed to perform operation", e);
}
```

7. 细化异常捕获顺序：`catch` 块是按照顺序执行的，所以应该从最具体的异常类型开始捕获，然后逐渐向上捕获更一般的异常类型。否则，具体的异常类型可能会被更一般的异常类型捕获，从而导致处理逻辑出错。

```java
try {
    // 可能抛出异常的代码
} catch (FileNotFoundException e) {
    // 处理 FileNotFoundException 的代码
} catch (IOException e) {
    // 处理 IOException 的代码
} catch (Exception e) {
    // 处理更一般的异常
}
```

了解 Java 异常的知识点、易错点以及如何正确地使用异常处理机制对于编写健壮、可维护的代码至关重要

## Error和Exception的区别

在 Java 中，`Error` 和 `Exception` 都是继承自 `Throwable` 类的子类，它们表示程序运行过程中可能遇到的问题。尽管它们都表示程序中的错误或异常情况，但它们之间存在一些关键区别：

1. 用途：

   - `Error`：表示程序运行过程中遇到的严重问题，**这些问题通常是 JVM（Java 虚拟机）或系统相关的，如内存溢出、虚拟机错误等。`Error` 表示的问题通常是无法预期或无法恢复的，程序员通常无法处理这些错误**。
   
   - `Exception`：表示程序运行过程中可能遇到的问题，这些问题通常是由程序逻辑错误或外部资源（如文件、网络连接等）引起的。`Exception` 表示的问题可以是预期的，程序员可以通过编写适当的代码来处理这些异常。

2. 处理方式：

   - `Error`：由于 `Error` 表示的问题通常是严重的且无法恢复的，因此程序员不需要（也通常无法）处理这些错误。当遇到 `Error` 时，程序通常会终止执行。
   
   - `Exception`：程序员可以使用 try-catch-finally 语句处理 `Exception`。Java 异常分为两种类型：受检异常（checked exceptions）和非受检异常（unchecked exceptions）。受检异常需要显式处理（使用 try-catch 语句或在方法声明中使用 `throws` 关键字），而非受检异常可以选择性处理。

3. 类层次结构：

   - `Error`：`Error` 类及其子类位于 Java 类层次结构中的 `java.lang` 包下。一些常见的 `Error` 子类包括 `OutOfMemoryError`、`StackOverflowError`、`LinkageError` 等。
   
   - `Exception`：`Exception` 类及其子类位于 Java 类层次结构中的 `java.lang` 包下。`Exception` 有很多子类，如 `IOException`、`SQLException`、`NullPointerException`、`IllegalArgumentException` 等。其中，`RuntimeException` 类是非受检异常的基类。

总之，`Error` 和 `Exception` 在 Java 中都表示程序运行过程中可能遇到的问题，但它们的用途、处理方式和类层次结构存在一些关键区别。`Error` 表示严重的、无法恢复的问题，通常无法处理；而 `Exception` 表示可以预期和处理的问题。

## 总结

本章主要讲了java异常的一些知识点,包括异常的定义,如果使用异常,捕获异常,自定义异常

# 第十章  IO 系统



## IO流

Java I/O（输入/输出）库提供了许多类来处理数据流。这些类可以分为字节流和字符流。以下是 Java I/O 流的用法、注意点和特点的总结。

1. 字节流（Byte Streams）：
   
   字节流用于处理原始二进制数据。它们的主要类是 InputStream 和 OutputStream。字节流的主要子类有：

   - **FileInputStream**：用于从文件中读取字节。
   - FileOutputStream：用于将字节写入文件。
   - ByteArrayInputStream：用于从字节数组中读取字节。
   - ByteArrayOutputStream：用于将字节写入字节数组。
   - BufferedInputStream：用于缓冲从其他输入流中读取的字节，以提高性能。
   - BufferedOutputStream：用于缓冲要写入其他输出流的字节，以提高性能。

   注意点和特点：
   
   - 字节流不处理字符编码，因此可能导致字符数据在读取或写入时出现乱码。
   - 在处理文本数据时，推荐使用字符流，因为它们能够更好地处理字符编码问题。
   - 为了避免资源泄漏，确保在使用完 I/O 流后正确地关闭它们。

2. 字符流（Character Streams）：

   字符流用于处理字符数据。它们的主要类是 Reader 和 Writer。字符流的主要子类有：

   - FileReader：用于从文件中读取字符。
   - FileWriter：用于将字符写入文件。
   - InputStreamReader：用于将字节流转换为字符流，可以指定字符编码。
   - OutputStreamWriter：用于将字符流转换为字节流，可以指定字符编码。
   - BufferedReader：用于缓冲从其他 Reader 中读取的字符，以提高性能。
   - BufferedWriter：用于缓冲要写入其他 Writer 的字符，以提高性能。
   - StringReader：用于从字符串中读取字符。
   - StringWriter：用于将字符写入字符串。

   注意点和特点：
   
   - 字符流可以处理字符编码，因此更适合处理文本数据。
   - InputStreamReader 和 OutputStreamWriter 类允许指定字符编码，以便在不同平台之间正确处理文本数据。
   - 为了避免资源泄漏，确保在使用完 I/O 流后正确地关闭它们。

除了上述基本的字节流和字符流类之外，Java I/O 还提供了许多实用的过滤器和适配器类，如 DataInputStream、DataOutputStream、PrintStream、PrintWriter 等，它们为特定类型的数据提供了更高级的功能。

在使用 Java I/O 流时，注意选择合适的流类型，并确保在使用完流后正确地关闭它们以避免资源泄漏。

## File类

`File` 类是 Java I/O 库中用于表示文件和目录路径名的抽象表示。以下是 `File` 类的主要用法：

1. 创建文件和目录：

   - `createNewFile()`：创建一个新的空文件，如果文件不存在。
   - `mkdir()`：创建一个新的目录，如果目录不存在。
   - `mkdirs()`：创建一个新的目录及其所有必需的父目录。

2. 文件和目录操作：

   - `renameTo(File dest)`：重命名文件或目录。
   - `delete()`：删除文件或目录。
   - `deleteOnExit()`：请求在 JVM 退出时删除文件或目录。

3. 获取文件和目录属性：

   - `exists()`：判断文件或目录是否存在。
   - `isFile()`：判断是否是文件。
   - `isDirectory()`：判断是否是目录。
   - `length()`：获取文件的长度（字节数）。
   - `getName()`：获取文件或目录的名称。
   - `getAbsolutePath()`：获取文件或目录的绝对路径。
   - `getPath()`：获取文件或目录的相对路径。
   - `getParent()`：获取文件或目录的父目录。
   - `lastModified()`：获取文件或目录的最后修改时间。
   - `list()`：获取目录中的文件和目录名列表。
   - `listFiles()`：获取目录中的 `File` 对象列表。
   - `list(FilenameFilter filter)`：使用指定的过滤器获取目录中的文件和目录名列表。
   - `listFiles(FileFilter filter)`：使用指定的过滤器获取目录中的 `File` 对象列表。

4. 设置文件和目录属性：

   - `setLastModified(long time)`：设置文件或目录的最后修改时间。
   - `setReadOnly()`：设置文件或目录为只读。
   - `setWritable(boolean writable)`：设置文件或目录的可写属性。
   - `setExecutable(boolean executable)`：设置文件或目录的可执行属性。

5. 检查文件权限：

   - `canRead()`：检查文件或目录是否可读。
   - `canWrite()`：检查文件或目录是否可写。
   - `canExecute()`：检查文件是否可执行。

这是 `File` 类的主要用法。在使用 `File` 类时，请注意正确处理异常（如 `IOException`），并在操作完成后关闭文件和释放资源。注意，虽然 `File` 类提供了许多文件和目录操作的方法，但在 Java NIO 的 `Path` 和 `Files` 类中，也提供了更现代且推荐使用的 API 来处理文件和目录。

# 第十一章 反射

## Class对象

在 Java 中，`Class` 对象是一个特殊的对象，用于表示加载到 Java 虚拟机 (JVM) 中的类的**元数据**。**`Class` 对象包含了与类相关的信息，如类名、类的父类、类实现的接口、类的字段、构造函数、方法等。每个加载到 JVM 中的类都有一个对应的 `Class` 对象。**

当 JVM 加载一个类时，它会创建一个 `Class` 对象来表示这个类。之后，您可以使用这个 `Class` 对象来获取有关该类的信息，实例化该类的对象，以及执行其他与类相关的操作。

要获取一个类的 `Class` 对象，可以使用以下方法之一：

1. 对于已知的类，可以使用 `.class` 语法获取其对应的 `Class` 对象。例如：

   ```java
   Class<?> stringClass = String.class;
   ```

2. 如果您有一个对象实例，可以调用该对象的 `getClass()` 方法来获取其对应的 `Class` 对象。例如：

   ```java
   String str = "Hello, World!";
   Class<?> objClass = str.getClass();
   ```

3. 如果您知道类的完全限定名（包括包名和类名），可以使用 `Class.forName()` 方法获取其 `Class` 对象。例如：

   ```java
   Class<?> clazz = Class.forName("java.lang.String");
   ```

获取到 `Class` 对象后，可以使用它的方法来获取类的信息，实例化对象，以及执行其他操作。一些常用的 `Class` 对象方法包括：

- `getName()`：获取类的完全限定名。
- `getSimpleName()`：获取类的简单名称。
- `getSuperclass()`：获取类的父类。
- `getInterfaces()`：获取类实现的接口。
- `getFields()`、`getMethods()`、`getConstructors()` 等：获取类的字段、方法、构造函数等。
- `newInstance()`：（已弃用）创建类的实例。建议使用 `getConstructor()` 方法获取构造函数，然后调用 `newInstance()` 方法创建对象。
- `isAssignableFrom(Class<?> cls)`：检查当前 `Class` 对象是否可以从指定的类赋值。
- `isInstance(Object obj)`：检查指定的对象是否是当前 `Class` 对象表示的类的实例。
- `cast(Object obj)`：将指定对象强制转换为当前 `Class` 对象表示的类的类型。

这些方法使您能够在运行时获取和操作类的信息。这种能力在编写通用代码、实现框架或执行动态操作时非常有用。

## 反射

Java 反射（Reflection）是一个强大的特性，允许在运行时检查和操作类、接口、字段和方法的信息。通过反射，您可以动态地创建对象、调用方法、获取和设置字段值等。这种能力在编写通用代码、实现框架或执行动态操作时非常有用。

以下是 Java 反射的一些主要用途：

1. 动态创建对象：通过反射，您可以在运行时动态地创建对象，而无需在编译时知道类的确切类型。例如：

   ```java
   Class<?> clazz = Class.forName("com.example.MyClass");
   Object obj = clazz.getConstructor().newInstance();
   ```

2. 获取和调用方法：您可以使用反射来获取类的方法，并在运行时动态地调用它们。例如：

   ```java
   Class<?> clazz = Class.forName("com.example.MyClass");
   Method method = clazz.getMethod("myMethod", String.class);
   Object result = method.invoke(obj, "Hello, World!");
   ```

3. 获取和设置字段值：反射允许您获取类的字段，并在运行时获取和设置它们的值。例如：

   ```java
   Class<?> clazz = Class.forName("com.example.MyClass");
   Field field = clazz.getField("myField");
   Object fieldValue = field.get(obj);
   field.set(obj, "New Value");
   ```

4. 获取注解:

   在 Java 中，注解（Annotation）的值在编译时确定，并存储在类文件中。在运行时，您可以使用反射来访问注解的值，但不能修改它们。注解的值被视为不可变，因此在运行时尝试更改它们将不起作用。

   要访问注解的值，您可以通过以下方法：

   1. 获取类上的注解：

      ```java
      Class<?> clazz = Class.forName("com.example.MyClass");
      MyAnnotation myAnnotation = clazz.getAnnotation(MyAnnotation.class);
      if (myAnnotation != null) {
          String value = myAnnotation.value();
          System.out.println("Value: " + value);
      }
      ```

   2. 获取方法上的注解：

      ```java
      Method method = clazz.getMethod("myMethod", String.class);
      MyAnnotation myAnnotation = method.getAnnotation(MyAnnotation.class);
      if (myAnnotation != null) {
          String value = myAnnotation.value();
          System.out.println("Value: " + value);
      }
      ```

   3. 获取字段上的注解：

      ```java
      Field field = clazz.getField("myField");
      MyAnnotation myAnnotation = field.getAnnotation(MyAnnotation.class);
      if (myAnnotation != null) {
          String value = myAnnotation.value();
          System.out.println("Value: " + value);
      }
      ```

   4. 获取构造函数上的注解：

      ```java
      Constructor<?> constructor = clazz.getConstructor();
      MyAnnotation myAnnotation = constructor.getAnnotation(MyAnnotation.class);
      if (myAnnotation != null) {
          String value = myAnnotation.value();
          System.out.println("Value: " + value);
      }
      ```

   

5. 动态代理：Java 反射还允许您在运行时动态地创建代理对象，以便在不修改原始类的情况下拦截和修改方法调用。例如，您可以使用 `java.lang.reflect.Proxy` 类来创建动态代理。

以下是使用 Java 反射时需要注意的一些事项：

1. 性能：反射操作通常比非反射操作慢，因为它们涉及到运行时类型检查和其他开销。因此，在关注性能的场景中，谨慎使用反射。

2. 安全：反射可能会破坏封装，因为它允许您访问和修改私有字段和方法。在使用反射时，请确保您遵循最佳实践，以防止意外地暴露敏感信息或破坏对象状态。

3. 兼容性：反射代码可能会更加脆弱，因为它依赖于在运行时确定的类型信息。如果类的结构发生变化（例如，字段或方法被重命名、移除或更改），反射代码可能会出现错误。在使用反射时，请确保您的代码能够适应这些变化，或者使用其他机制（如接口或依赖注入）来减小耦合度。

尽管 Java 反射具有一定的复杂性和潜在风险，但在许多场景下，它为您提供了强大的动态编程能力

## 总结

本章主要讲了元类与元类提供的方法, 元类是对一个类的描述,我们可以通过元类获取类定义的一些信息,比如注解,字段,方法,从而可以动态的对一个对象做一些事情



# 第十二章 克隆

在 Java 里面，克隆（Clone）是一种创建对象副本的过程。在 Java 中，克隆主要通过实现 `java.lang.Cloneable` 接口和覆盖 `clone()` 方法来实现。

克隆的主要作用是在以下场景中：

1. **创建独立副本**：当你需要创建一个对象的副本，与原对象相互独立，以便在不影响原对象的情况下对副本进行修改。

2. **优化性能**：如果创建一个对象的过程非常耗时，可以通过克隆已有的对象来节省时间和资源。

3. **保护对象状态**：当一个对象需要与其他对象共享，但又不希望其他对象更改其状态时，**可以提供一个副本供其他对象使用**。

Java 的克隆分为浅克隆（Shallow Clone）和深克隆（Deep Clone）：

- 浅克隆：只复制对象本身，不复制对象内部引用的其他对象。这意味着原对象和克隆对象共享同一个引用类型的成员变量。

- 深克隆：复制对象及其内部引用的所有对象。这样，原对象和克隆对象不会共享任何引用类型的成员变量。

## 浅克隆

要使用克隆功能，请实现 `Cloneable` 接口，并覆盖 `clone()` 方法。例如：

```java
class MyClass implements Cloneable {
    // 类成员和方法

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}
```

这样，可以通过调用 `clone()` 方法创建对象的副本：

```java
MyClass original = new MyClass();
MyClass copy = (MyClass) original.clone();
```

## 深度克隆

在 Java 中，深克隆（Deep Clone）是指创建一个对象的副本，同时复制该对象及其所有引用的对象。实现深克隆有多种方法，以下是两种常见的方法：

方法一：使用序列化和反序列化

要使用这种方法，首先需要让你的类实现 `java.io.Serializable` 接口。然后，通过将对象序列化到字节流中，再从字节流中反序列化回对象，实现深克隆。示例如下：

```java
import java.io.*;

public class DeepCopyUtil {
    public static Object deepClone(Object object) {
        try {
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(baos);
            oos.writeObject(object);
            oos.close();

            ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
            ObjectInputStream ois = new ObjectInputStream(bais);
            Object clonedObject = ois.readObject();
            ois.close();

            return clonedObject;
        } catch (IOException | ClassNotFoundException e) {
            throw new RuntimeException("Deep clone failed.", e);
        }
    }
}
```

方法二：递归克隆

对于每个引用类型的成员变量，实现它们各自的深克隆方法。然后，在覆盖的 `clone()` 方法中递归地调用这些方法。示例如下：

```java
class MyClass implements Cloneable {
    private AnotherClass anotherClass;

    public MyClass(AnotherClass anotherClass) {
        this.anotherClass = anotherClass;
    }

    // 其他方法

    @Override
    protected Object clone() throws CloneNotSupportedException {
        MyClass cloned = (MyClass) super.clone();
        cloned.anotherClass = (AnotherClass) this.anotherClass.clone();
        return cloned;
    }
}

class AnotherClass implements Cloneable {
    // 类成员和方法

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}
```

在这个例子中，`MyClass` 类包含一个引用类型的成员变量 `anotherClass`。我们分别在 `MyClass` 和 `AnotherClass` 中覆盖了 `clone()` 方法，以实现深克隆。当调用 `MyClass` 类的 `clone()` 方法时，它会递归地调用 `AnotherClass` 类的 `clone()` 方法，从而实现深克隆。

注意：深克隆可能会引发性能问题，特别是在处理大型对象图时。在使用深克隆时，请务必权衡好性能与功能之间的平衡。

注意：克隆功能需要谨慎使用，因为它可能导致不可预期的副作用，例如多余的对象创建、内存泄漏等问题。有时，可以考虑使用其他设计模式（如原型模式、工厂模式等）替代克隆。

# 第十四章 多线程

Java 线程是 Java 平台提供的一种基本的并发编程单元。线程允许您在同一个程序中同时执行多个任务。以下是一些关于 Java 线程的核心知识点：

1. 线程的创建和启动

   在 Java 中，有两种主要的方法来创建线程：

   - 继承 `java.lang.Thread` 类并覆盖其 `run()` 方法。创建该类的实例并调用 `start()` 方法启动线程。
   - 实现 `java.lang.Runnable` 接口并实现其 `run()` 方法。将实现 `Runnable` 的类的实例传递给 `Thread` 类的构造函数，然后调用 `start()` 方法启动线程。

2. 线程的生命周期

   Java 线程有以下几种状态：

   - 新建（New）：线程对象已创建，但尚未启动。
   - 可运行（Runnable）：线程已启动，正在等待操作系统分配 CPU 时间片进行执行。
   - 阻塞（Blocked）：线程正在等待获取对象的监视器锁，以进入同步块或同步方法。
   - 等待（Waiting）：线程处于无限期等待状态，直到满足某个条件。例如，调用了 `wait()`、`join()` 或 `LockSupport.park()` 方法。
   - 超时等待（Timed Waiting）：线程处于有时间限制的等待状态。例如，调用了 `sleep()`、`wait(long)` 或 `join(long)` 方法。
   - 终止（Terminated）：线程执行完成或因异常而终止。

3. 线程的优先级

   Java 线程具有优先级，范围从 1（最低）到 10（最高）。默认情况下，线程的优先级设置为 5（普通优先级）。可以使用 `Thread.setPriority(int)` 方法设置线程的优先级。操作系统将根据线程的优先级分配 CPU 时间片。但**是这个不是一定的,不是说优先级越高,你就一定先获得CPU的时间片**

4. 同步和锁

   当多个线程需要访问共享资源时，可能会导致竞态条件和数据不一致。要解决这个问题，可以使用同步来确保同一时间只有一个线程能访问特定资源。Java 提供了以下同步机制：

   - 同步方法：使用 `synchronized` 关键字修饰方法。当线程调用同步方法时，需要获得该方法所属对象的监视器锁。
   - 同步块：使用 `synchronized` 关键字和一个锁对象来创建同步块。进入同步块时，线程需要获得锁对象的监视器锁。

5. 线程间通信

   Java 提供了以下机制来实现线程间通信：

   - `wait()`、`notify()` 和 `notifyAll()`：这些方法用于线程间的协作，让一个线程等待特定条件，而另一个线程在条件满足时唤醒等待的线程。这些方法必须在同步块或同步方法中使用。

6. 线程局部变量

   `java.lang.ThreadLocal` 类允许每个线程拥有自己的变量副本。当多个线程需要访问相同的变量，但又需要独立副本时，可以使用线程局部变量。这有助于减少竞态条件和同步的需求。

7. 线程安全的集合

   Java 提供了线程安全的集合类，如 `java.util.concurrent.ConcurrentHashMap`、`java.util.concurrent.CopyOnWriteArrayList` 等。这些集合在内部实现了同步和其他并发控制机制，以确保在多线程环境下的安全使用。

8. 线程池和 Executor 框架

   使用线程池可以有效地控制并发线程的数量，并在需要时重用线程。`java.util.concurrent.Executor` 和 `java.util.concurrent.ExecutorService` 接口提供了一个框架来管理和控制线程池。`java.util.concurrent.Executors` 类提供了工厂方法来创建不同类型的线程池，如固定大小的线程池、缓存的线程池等。

9. 并发工具类

   Java 并发库提供了许多高级并发工具类，如信号量（`java.util.concurrent.Semaphore`）、倒计时闩（`java.util.concurrent.CountDownLatch`）、循环屏障（`java.util.concurrent.CyclicBarrier`）等。这些类提供了强大的功能，以帮助解决复杂的多线程问题。

10. CompletableFuture

    `java.util.concurrent.CompletableFuture` 类提供了一种基于回调的异步编程模型。它允许您使用非阻塞操作来编写并发代码，并在操作完成时获得通知。

11. 并行流

    Java 8 引入了 Stream API，该 API 提供了一种简洁的方式来处理集合和数据流。Java 8 还提供了并行流（Parallel Stream），它允许您轻松地将顺序流转换为并行流，以便利用多核处理器并行处理数据。

# 第十五章 网络编程

Java 网络编程主要关注如何在 Java 应用程序中实现数据的传输和通信。以下是 Java 网络编程的主要知识点：

1. OSI 参考模型和 TCP/IP 协议栈：了解网络通信的基本原理和各层协议是学习 Java 网络编程的基础。
2. InetAddress 类：该类用于表示互联网协议（IP）地址。它提供了用于解析主机名和 IP 地址的方法。
3. 套接字（Socket）：Java 网络编程的核心是套接字，它是网络通信的端点。Java 提供了以下套接字类：

   - Socket：用于实现客户端的 TCP 套接字。它允许您建立到远程服务器的连接并发送/接收数据。
   - ServerSocket：用于实现服务器端的 TCP 套接字。它允许您监听来自客户端的连接并接收/发送数据。
   - DatagramSocket：用于实现基于 UDP 的无连接通信。它允许您发送/接收数据报文。
4. Java I/O 流：在 Java 网络编程中，常使用 I/O 流进行数据的读取和发送。以下是常用的 I/O 流：

   - InputStream 和 OutputStream：基本的字节流，用于读取和写入原始字节数据。
   - InputStreamReader 和 OutputStreamWriter：用于处理字符数据的字符流，将字节流转换为字符流。
   - BufferedReader 和 BufferedWriter：带缓冲的字符流，提高 I/O 性能。
   - DataInputStream 和 DataOutputStream：用于处理基本数据类型和字符串的数据流。
5. URL 和 HttpURLConnection：用于处理 HTTP 协议的类。URL 类表示统一资源定位符，可以用于访问网络资源。HttpURLConnection 类提供了发送 HTTP 请求和接收 HTTP 响应的功能。
6. 多线程：在网络编程中，通常需要使用多线程来处理并发连接和请求。了解如何在 Java 中创建和管理线程是网络编程的重要知识点。
7. Java NIO：Java 新输入输出（NIO）框架提供了高性能、非阻塞的 I/O 操作。Java NIO 主要包括 Channel、Buffer 和 Selector 等组件，它们允许您实现高效的网络通信。

以下是使用 Java 编程实现 TCP 和 UDP 通信的简单示例。

## TCP 示例：

客户端：
```java
import java.io.*;
import java.net.*;

public class TCPClient {
    public static void main(String[] args) throws IOException {
        // 创建一个连接到指定服务器和端口的套接字
        Socket socket = new Socket("localhost", 8080);
        
        // 获取输出流以发送数据到服务器
        OutputStream outputStream = socket.getOutputStream();
        PrintWriter writer = new PrintWriter(outputStream, true);
        
        // 发送消息到服务器
        writer.println("Hello, server!");

        // 获取输入流以接收服务器的响应
        InputStream inputStream = socket.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
        
        // 读取并输出服务器的响应
        String response = reader.readLine();
        System.out.println("Server response: " + response);

        // 关闭资源
        reader.close();
        writer.close();
        socket.close();
    }
}
```

服务器：
```java
import java.io.*;
import java.net.*;

public class TCPServer {
    public static void main(String[] args) throws IOException {
        // 创建一个在指定端口监听的 ServerSocket
        ServerSocket serverSocket = new ServerSocket(8080);

        // 等待客户端连接
        System.out.println("Waiting for a client...");
        Socket clientSocket = serverSocket.accept();
        System.out.println("Client connected.");

        // 获取输入流以接收客户端发送的数据
        InputStream inputStream = clientSocket.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));

        // 读取客户端发送的消息
        String message = reader.readLine();
        System.out.println("Client message: " + message);

        // 获取输出流以向客户端发送响应
        OutputStream outputStream = clientSocket.getOutputStream();
        PrintWriter writer = new PrintWriter(outputStream, true);

        // 向客户端发送响应
        writer.println("Hello, client!");

        // 关闭资源
        reader.close();
        writer.close();
        clientSocket.close();
        serverSocket.close();
    }
}
```

## UDP 示例：

发送方（客户端）：
```java
import java.io.IOException;
import java.net.*;

public class UDPSender {
    public static void main(String[] args) throws IOException {
        // 创建一个 DatagramSocket
        DatagramSocket datagramSocket = new DatagramSocket();

        // 准备发送的数据和目标地址
        String message = "Hello, receiver!";
        InetAddress address = InetAddress.getByName("localhost");
        int port = 8080;

        // 将数据转换为字节数组并创建一个 DatagramPacket
        byte[] buffer = message.getBytes();
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length, address, port);

        // 发送数据报
        datagramSocket.send(packet);
        System.out.println("Message sent.");

        // 准备接收响应
        byte[] responseBuffer = new byte[1024];
        DatagramPacket responsePacket = new DatagramPacket(responseBuffer, responseBuffer.length);

        // 接收响应数据报
        datagramSocket.receive(responsePacket);
        System.out.println("Response received.");

        // 从响应数据报中提取数据并转换为字符串
        String response = new String(responsePacket.getData(), 0, responsePacket.getLength());
        System.out.println("Response content: " + response);

        // 关闭资源
        datagramSocket.close();
    }
}

```

接收方（服务器）：
```java
import java.io.IOException;
import java.net.*;

public class UDPReceiver {
    public static void main(String[] args) throws IOException {
        // 创建一个在指定端口监听的 DatagramSocket
        int port = 8080;
        DatagramSocket datagramSocket = new DatagramSocket(port);

        // 准备接收数据报的缓冲区和 DatagramPacket
        byte[] buffer = new byte[1024];
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length);

        // 接收数据报
        datagramSocket.receive(packet);
        System.out.println("Message received.");

        // 从数据报中提取数据并转换为字符串
        String message = new String(packet.getData(), 0, packet.getLength());
        System.out.println("Message content: " + message);

        // 准备发送响应
        String response = "Hello, sender!";
        byte[] responseBuffer = response.getBytes();
        InetAddress senderAddress = packet.getAddress();
        int senderPort = packet.getPort();
        DatagramPacket responsePacket = new DatagramPacket(responseBuffer, responseBuffer.length, senderAddress, senderPort);

        // 发送响应数据报
        datagramSocket.send(responsePacket);
        System.out.println("Response sent.");

        // 关闭资源
        datagramSocket.close();
    }
}


       
```

# 补充

## 注解

Java 注解（Annotation）是一种为代码添加元数据的机制。它们可以用于提供额外的信息，**以便在编译时或运行时进行处理。注解可以应用于类、方法、字段、参数和其他代码元素**。以下是关于 Java 注解的一些关键概念和用法：

1. 定义注解：

   要定义注解，需要使用 `@interface` 关键字。注解可以具有属性（也称为元素），这些属性看起来像方法，但实际上是定义了注解的一部分。属性可以具有默认值。

   ```java
   import java.lang.annotation.*;
   
   @Retention(RetentionPolicy.RUNTIME)
   @Target(ElementType.TYPE)
   public @interface MyAnnotation {
       String value() default "default_value";
       String[] tags() default {};
       int priority() default 0;
   }
   ```

   以上代码定义了一个名为 `MyAnnotation` 的注解，具有 `value`、`tags` 和 `priority` 属性。

2. 应用注解：

   一旦定义了注解，就可以将其应用于代码元素（如类、方法、字段等）。例如：

   ```java
   @MyAnnotation(value = "example", tags = {"tag1", "tag2"}, priority = 1)
   public class MyClass {
       @MyAnnotation("field_annotation")  // 默认赋值给value
       private String myField;
   
       @MyAnnotation
       public void myMethod() {
           // ...
       }
   }
   ```

3. 元注解

   1. `@Retention`：指定注解的保留策略。可能的取值包括：

      - `RetentionPolicy.SOURCE`：注解仅在源代码中可用，编译器会在编译时丢弃它。
      - `RetentionPolicy.CLASS`：注解在编译后的类文件中可用，但 JVM 在运行时不保留它。这是默认保留策略。
      - `RetentionPolicy.RUNTIME`：注解在运行时可用，因此可以通过反射访问。

   2. `@Target`：限制注解可以应用的 Java 元素类型。可能的取值包括：

      - `ElementType.TYPE`：类、接口、枚举或注解。
      - `ElementType.FIELD`：字段。
      - `ElementType.METHOD`：方法。
      - `ElementType.PARAMETER`：方法参数。
      - `ElementType.CONSTRUCTOR`：构造函数。
      - `ElementType.LOCAL_VARIABLE`：局部变量。
      - `ElementType.ANNOTATION_TYPE`：注解类型。
      - `ElementType.PACKAGE`：包。
      - `ElementType.TYPE_PARAMETER`：类型参数（Java 8 及更高版本）。
      - `ElementType.TYPE_USE`：类型使用（Java 8 及更高版本）。

   3. `@Documented`：将注解信息包含在 Javadoc 文档中。此元注解没有取值。

   4. `@Inherited`：表示注解可从父类继承。此元注解没有取值。请注意，`@Inherited` 仅对类注解有效，对方法、字段和构造函数注解无效。

   5. `@Repeatable`：表示注解可以在同一个元素上多次使用。它的取值是一个容器注解，该容器注解用于存储重复注解。

## 泛型

泛型（Generics）是 Java 5 引入的一项功能，**它允许在编译时进行类型检查。泛型的主要目标是提高代码的类型安全性和可重用性**。在这里，我们将全面了解泛型的概念、优点和使用方法。

1. 什么是泛型？

泛型允许开发人员在类、接口和方法中使用类型参数。类型参数是一个占位符，可以在实例化或调用泛型类型时指定具体类型。这样，可以编写一次代码，然后在不同情况下重用它，而无需修改源代码。

2. 泛型类和泛型接口：

泛型类和泛型接口是使用类型参数定义的类和接口。例如：

```java
public class GenericBox<T> {
    private T item;

    public void setItem(T item) {
        this.item = item;
    }

    public T getItem() {
        return item;
    }
}

public interface GenericComparator<T> {
    int compare(T a, T b);
}
```

3. 泛型方法：

泛型方法是在方法签名中使用类型参数定义的方法。泛型方法可以在泛型类、泛型接口或普通类中定义。例如：

```java
public class GenericUtils {
    public static <T> T getFirst(List<T> list) {
        return list.get(0);
    }
}
```

4. 类型擦除：

为了确保与没有使用泛型的旧代码兼容，**Java 编译器在编译泛型代码时会执行类型擦除**。**类型擦除意味着编译器将泛型类型参数替换为其限定类型（通常是 Object）或限定类型的上界。因此，在运行时，泛型信息被擦除，不能在运行时查询泛型类型信息**。

5. 有界类型参数：

有时，我们希望限制泛型类型参数可以使用的类型。可以通过在类型参数后面添加 extends 关键字和相应的限定类型来实现这一目标。例如：

```java
public class GenericBox<T extends Comparable<T>> {
    // ...
}
```

> 这里表示T必须是Comparable的子类型 也就是说T得是Comparable的子类或者接口实现

6. 通配符：

通配符是一种特殊的类型参数，用于表示未知类型。通配符在泛型类型中表示为问号（?）。通配符分为三类：

   - 无限制通配符：`<?>`，表示任何类型。
   - 上界通配符：`<? extends T>`，表示 T 或其子类。
   - 下界通配符：`<? super T>`，表示 T 或其超类。

7. 泛型的优势：

   - 类型安全：泛型在编译时进行类型检查，从而减少了在运行时由于类型不匹配引发的错误。
   - 代码重用：可以使用泛型编写一段代码，然后在不同的类型场景中重用它。

      - 提高代码可读性：泛型使代码更具可读性，因为它明确地指定了类型，有助于理解代码的预期行为和功能。

8. 泛型限制：

虽然泛型提供了许多优势，但它也有一些限制：

   - 由于类型擦除，泛型类型参数在运行时不可用。这意味着不能在运行时查询泛型类型信息。
   - 不能实例化泛型类型参数。例如，不能使用 `new T()`。
   - 不能创建泛型数组。例如，不能创建 `T[]` 类型的数组。
   - 不能将基本类型用作泛型类型参数。必须使用相应的包装类，如 `Integer`、`Double` 等。

9. PECS（Producer Extends Consumer Super）原则：

PECS 原则是一种关于如何使用通配符的经验法则。它表示：

   - 当你需要从泛型类型中获取（生产）数据时，使用 `extends`（上界通配符）。
   - 当你需要将数据放入（消费）泛型类型中时，使用 `super`（下界通配符）。

这个原则有助于确保泛型类型在生产和消费数据时的类型安全性。

总结一下，泛型是 Java 中非常重要的特性，它提高了代码的类型安全性、可重用性和可读性。通过掌握泛型类、泛型接口、泛型方法、类型擦除、有界类型参数、通配符、泛型的优势和限制，以及 PECS 原则，你将能够更有效地使用泛型来编写高质量的 Java 代码。

## 类的加载

类的加载是 Java 运行时环境在执行 Java 程序时将类加载到 Java 虚拟机（JVM）中的过程。类的加载包括以下几个阶段：

1. 加载（Loading）：JVM 从文件系统、网络或其他资源中加载类的二进制数据（字节码文件），并根据这些数据在 JVM 内存中创建一个 java.lang.Class 对象。这个阶段主要由类加载器（Class Loader）完成。仅导入类（使用 import 语句）不会触发类加载，类加载发生在实际使用类时，如创建对象、访问静态变量或方法等。

2. 验证（Verification）：在加载阶段之后，JVM 对字节码文件进行验证，确保它符合 Java 语言规范，不包含非法指令，保证其正确性和安全性。

3. 准备（Preparation）：在验证阶段之后，JVM 为类的静态变量分配内存并设置默认值。例如，对于基本类型的静态变量，整数型变量会被设置为 0，浮点型变量会被设置为 0.0，布尔型变量会被设置为 false，引用类型变量会被设置为 null。

4. 解析（Resolution）：在准备阶段之后，JVM 对类中的符号引用进行解析，将其替换为直接引用。符号引用是指用类、字段或方法的名字和描述符来表示，而直接引用是指用内存地址或偏移量来表示。解析阶段保证了类、字段和方法的使用可以被正确地定位。

5. 初始化（Initialization）：在解析阶段之后，JVM 对类进行初始化，执行类的静态代码块和静态变量赋值操作。这些操作按照它们在类中出现的顺序执行。

在 Java 中，**类的加载通常是惰性的（按需加载）。这意味着类在实际使用之前不会被加载。仅导入类（使用 import 语句）不会触发类的加载**。类加载发生在以下情况：

- 创建类的实例（使用 new 关键字）。
- **访问类的静态变量**。
- **调用类的静态方法**。
- **使用反射来创建实例、访问变量或调用方法。**
- **初始化子类时，父类会先被加载**。

当类被加载到 JVM 时，只有在实际使用类的过程中，类的加载才被认为已经完成。

## jar包

要将 Java 程序打包成 JAR 文件，您可以使用 JDK 提供的 `jar` 命令。以下是一个简单的步骤：

1. 确保您已经编译了 Java 源代码，生成了 `.class` 文件。

2. 创建一个名为 `manifest.txt` 的清单文件，其中包含一个 `Main-Class` 项，指定应用程序的入口类。例如，如果您的程序入口类为 `com.example.Main`，则 `manifest.txt` 文件的内容应为：
   ```
   Main-Class: com.example.Main
   ```

   > 文件内容可以没有,但是文件一定要有

3. 使用 `jar` 命令创建 JAR 文件。将 `-c`（创建新的 JAR 文件）、`-v`（详细输出）和 `-f`（指定 JAR 文件名）选项与清单文件和要打包的 `.class` 文件一起传递。 **可以传递多个文件,不限于.class文件**

   ```
   jar -cvfm myprogram.jar manifest.txt com/example/*.class test.txt
   ```
   这个命令将创建一个名为 `myprogram.jar` 的 JAR 文件，包含 `manifest.txt` 清单文件和 `com/example` 目录下的所有 `.class` 文件。

4. 确认 JAR 文件已成功创建。可以使用 `jar` 命令的 `-t`（列出 JAR 文件内容）选项查看 JAR 文件中的文件：
   ```
   jar -tvf myprogram.jar
   ```

5. 使用 `java` 命令运行 JAR 文件：
   ```
   java -jar myprogram.jar
   ```
   这个命令将启动 Java 虚拟机并运行 `myprogram.jar` 中指定的 `Main-Class`。

注意：如果您的应用程序依赖于其他 JAR 文件或类文件，需要在运行 JAR 文件时通过 `-classpath` 或 `-cp` 参数指定这些依赖项。例如：

```
java -classpath library.jar -jar myprogram.jar
```



## 命令用法

`java` 和 `javac` 是 Java 开发者在命令行中经常使用的两个命令。`javac` 是 Java 编译器，用于将 Java 源代码文件编译成 Java 字节码文件（`.class` 文件）。`java` 命令用于启动 Java 虚拟机（JVM），加载和执行 Java 程序。

下面是一些`java` 和 `javac` 命令常用用法：

**javac 命令：**

1. 编译单个 Java 源文件：
   ```
   javac Main.java
   ```
   这个命令将 `Main.java` 源文件编译成 `Main.class` 字节码文件。

2. 编译多个 Java 源文件：
   ```
   javac Main.java Test.java
   ```
   这个命令将同时编译 `Main.java` 和 `Test.java` 源文件。

3. 编译指定目录下的所有 Java 源文件：
   ```
   javac -sourcepath ./src -d ./bin ./src/**/*.java
   ```
   这个命令将编译 `src` 目录下的所有 Java 源文件，并将生成的 `.class` 文件存放到 `bin` 目录下。

4. 指定编译时的类路径：
   ```
   javac -classpath lib/* Main.java
   ```
   这个命令将在编译 `Main.java` 时使用 `lib` 目录下的所有 JAR 文件作为类路径。**如果用了这个命令我们在执行java的时候也要指定classpath路径**

> 使用javac的时候,依赖的库只需要是.class文件, 但是他会去对比.class文件与.java文件的日期,如果.class文件旧与.java文件,他会把java文件也编译了

**java 命令：**

1. 执行 Java 程序：
   ```
   java Main
   ```
   这个命令将运行 `Main.class` 文件中的 `main` 方法。

2. 指定运行时的类路径：
   ```
   java -classpath lib/* Main
   ```
   这个命令将在执行 `Main` 类时使用 `lib` 目录下的所有 JAR 文件作为类路径。

3. 设置 Java 虚拟机启动参数：
   ```
   java -Xms128m -Xmx512m Main
   ```
   这个命令将在启动 Java 虚拟机时设置初始堆内存为 128 MB，最大堆内存为 512 MB。

4. 启动带有命令行参数的 Java 程序：
   ```
   java Main arg1 arg2 arg3
   ```
   这个命令将把 `arg1`、`arg2` 和 `arg3` 作为命令行参数传递给 `Main` 类的 `main` 方法。

5. **更改当前工作目录**：**这样的话可以更改文件读写的位置,不会影响类路径**,这可以通过设置 JVM 参数 `user.dir` 来实现。例如，在启动 Java 程序时，可以使用以下命令：

   ```
   java -Duser.dir=/path/to/your/directory YourMainClass
   ```

   请注意，这种方法在程序运行时更改当前工作目录的能力有限，因为它取决于 JVM 的实现。

这些是 `java` 和 `javac` 命令的一些常用选项。实际上，这两个命令还有许多其他选项和功能，您可以在官方文档中找到更详细的信息。



## 相关概念

让我们详细讨论 Java 中的包、类路径和执行机制。

1. 包（Package）：
   
   **包是 Java 中用于组织和分类类的一种方式。包名的目的是为了避免命名冲突和提高代码的可读性**。**Java 包名通常遵循域名的反序**，例如：`com.example.myapp`。包名对应的目录结构是以点（`.`）分隔的子目录，如：`com/example/myapp`。

2. Java 源文件和类文件的组织：

   在 Java 项目中，源文件（`.java`）和类文件（`.class`）通常按照包名的目录结构进行组织。例如，包名为 `com.djm.test` 的源文件应位于 `src/com/djm/test` 目录下。编译后的类文件通常放在一个单独的目录中，如 `out/com/djm/test`。

3. 类路径（Classpath）：

   类路径是 Java 运行时用于查找类文件的路径设置。Java 运行时会根据类路径的设置在文件系统或其他位置查找 `.class` 文件。类路径可以通过设置环境变量 `CLASSPATH` 或使用命令行选项 `-cp` 或 `-classpath` 来指定。

   默认情况下，类路径包含当前目录（`.`）。这意味着，如果没有指定类路径，Java 运行时会从当前目录开始查找类文件。

4. 执行 Java 程序：

   当使用 `java` 命令执行 Java 程序时，需要提供主类的全名（包括包名和类名）。例如，如果主类 `Main` 位于 `com.djm.test` 包中，执行命令应该是 `java com.djm.test.Main`。

   如果类路径设置正确，Java 运行时会在类路径中查找主类的 `.class` 文件。如果找不到主类，会报错。

**所以我们在执行java命令的时候 一定要指明包名和类名**, 根据包名我们就应该要知道我们要在哪个位置执行java命令,比如我有个java文件,设置包名为 com.djm.test  那么我门就要在这个文件的上4层目录下执行,这个目录还具有com/djm/test子目录,所以我们不要随便设置包名,而是要根据项目所在位置下面 的目录文件命名,然后再项目目录下执行文件

## 关于classpath

`classpath`（类路径）是 Java 运行时环境用来查找类和其他资源的一个参数。当 Java 运行时环境需要加载类或资源时，它会根据 `classpath` 中的设置在文件系统或其他位置查找对应的文件。`classpath` 可以包含目录、JAR 文件或其他资源。以下是 Java 会选择的几个默认类路径：

1. **当前目录**：默认情况下，Java 运行时环境会将当前目录（`.`）包含在类路径中。这意味着 Java 会在运行程序的当前目录中查找类和资源。

2. **Java 标准库**：Java 运行时环境还会在 Java 标准库（JRE 或 JDK 中的 `lib` 目录）中查找类和资源。这些库包含 Java 标准类，如 `java.util.ArrayList`、`java.lang.String` 等。

3. **用户定义的类路径**：用户可以通过设置 `CLASSPATH` 环境变量或使用命令行选项 `-cp` 或 `-classpath` 来定义自己的类路径。例如：

   ```
   java -cp /path/to/my/classes:/path/to/my/libs/mylib.jar MyMainClass
   ```

   在这个例子中，Java 会在 `/path/to/my/classes` 目录和 `/path/to/my/libs/mylib.jar` JAR 文件中查找类和资源。**使用了自定义的类路径后,当前目录就不会被加入到类路径中**

   > java标准库的优先级是高于默认和自定义的类路径的,只要在最前面找到了class文件,就不会继续往后面找

需要注意的是，不同操作系统中，类路径的分隔符可能不同。在 Windows 中，类路径的分隔符是分号（`;`），而在 Unix 和类 Unix 系统（如 Linux 和 macOS）中，类路径的分隔符是冒号（`:`）。

总之，Java 会根据当前目录、Java 标准库和用户定义的类路径设置来确定类路径。当需要加载类或资源时，Java 会根据这些设置在文件系统或其他位置查找对应的文件。

## java 命令执行流程

当使用 `java` 命令执行 Java 程序时，Java 运行时会执行以下步骤：

1. 加载 Java 虚拟机（JVM）：首先，Java 运行时会加载 Java 虚拟机，它负责执行 Java 字节码。
2. 设置类路径：Java 运行时会设置类路径（classpath），这是一个包含 Java 类文件（如 `.class` 文件）的目录和文件列表。类路径是 Java 运行时用于查找类文件的路径设置。
3. 加载主类：Java 运行时会尝试在类路径中查找指定的主类（包括包名和类名）。例如，如果执行的命令是 `java com.djm.test.Main`，Java 运行时将在类路径中查找 `com.djm.test.Main` 类,也就是 在类路径下com/djm/test/下找到 Main.class,如果找不到就会报错,**找到后会验证Main.class的包名是否跟执行包名一样**,不一样也会报错
4. 链接：链接过程包括验证、准备和解析三个阶段。验证确保类文件的结构和约束符合 Java 虚拟机规范；准备阶段为类变量分配内存并设置默认初始值；解析阶段将类中的符号引用解析为直接引用。
5. 初始化：Java 运行时会初始化类，这包括执行类的静态初始化代码（例如静态变量的初始化和静态代码块）。
6. 执行主方法：Java 运行时会找到主类中的 `main` 方法（它必须具有 `public static void main(String[] args)` 的签名），并执行它。这是 Java 程序的入口点。
7. 执行程序：`main` 方法开始执行，程序按照您编写的代码逻辑进行运行。
8. 垃圾回收：Java 程序在运行过程中，Java 虚拟机会自动进行垃圾回收，回收不再使用的对象占用的内存。
9. 程序结束：当 `main` 方法执行完毕或者调用了 `System.exit()` 方法，Java 程序结束，Java 虚拟机关闭，释放相关资源。

这些步骤概括了使用 `java` 命令执行 Java 程序的整个过程。在这个过程中，Java 运行时负责管理内存、执行字节码和处理异常等任务。

## jdk jre jvm

JDK（Java Development Kit）、JRE（Java Runtime Environment）和 JVM（Java Virtual Machine）是 Java 平台的三个核心组成部分。它们之间存在联系，但也有区别。下面我们详细讨论这三个组件：

1. JVM（Java Virtual Machine）：
   - Java 虚拟机是 Java 平台的基础，它为 Java 字节码提供了一个运行时环境。JVM 负责将 Java 字节码（.class 文件）翻译成与特定硬件和操作系统相对应的本地机器代码。
   - JVM 是平台无关的，不同的操作系统和硬件平台都有相应的 JVM 实现。这使得 Java 应用程序能够跨平台运行（“一次编写，到处运行”）。
   - JVM 还负责管理 Java 程序的内存分配和垃圾回收。

2. JRE（Java Runtime Environment）：
   - Java 运行时环境包括 JVM 以及 Java 类库（java.util、java.lang、java.io 等）和其他运行 Java 应用程序所需的文件。
   - JRE 允许用户在没有安装 JDK 的情况下运行 Java 程序。这意味着用户只需要 JRE 就可以运行 Java 应用程序，而无需 JDK。
   - JRE 不包括开发工具，如编译器（javac）或调试器。因此，如果要开发 Java 程序，需要 JDK。

3. JDK（Java Development Kit）：
   - Java 开发工具包是 Java 开发人员使用的完整软件开发包，包括 JRE、编译器（javac）、调试器、文档生成器（javadoc）以及其他开发和调试 Java 程序所需的工具。
   - JDK 是开发 Java 应用程序所需的最低要求。它包含了 JRE，因此安装 JDK 时，无需单独安装 JRE。

总结一下：
- JVM 是 Java 虚拟机，提供了运行 Java 字节码的环境，并负责内存管理和垃圾回收。
- JRE 是 Java 运行时环境，包括 JVM 和 Java 类库，用于运行 Java 程序。
- JDK 是 Java 开发工具包，包括 JRE 和开发工具（编译器、调试器等），用于开发 Java 程序。

JDK、JRE 和 JVM 之间的关系是：JDK 包含 JRE，JRE 包含 JVM。在 Java 开发和运行过程中，这三者共同协作，使得 Java 程序能够跨平台运行。

## 路径问题

### 相对路径

当我们使用OutputSream 和 InputStream 的时候,如果是相对路径的话,默认是从**java执行命令下路径下读写文件**,在idea中它自己帮我们重新设置了user.dir,**因此就是相对项目路径**

> 如果是以/开头比如 /a 是绝对路径 一般表示c盘的根目录

### 类路径

类路径（Classpath）：类路径是 JVM 用来**搜索类和资源文件**的路径。类路径可以包含目录、JAR 文件和其他资源。可以使用 `System.getProperty("java.class.path")` 获取当前的类路径。

要从类路径加载资源文件，可以使用 `ClassLoader` 类的 `getResource()` 或 `getResourceAsStream()` 方法。这些方法将从类路径中查找资源，而不依赖于当前工作目录。例如，以下代码将尝试从类路径中加载一个名为 `config.properties` 的文件：

```java
InputStream is = getClass().getClassLoader().getResourceAsStream("config.properties");
```

当使用类路径加载资源时，请确保资源文件已被包含在类路径中。对于 Java 项目，通常将资源文件放在 `src/main/resources` 目录下，以便它们在构建过程中被正确地处理。

## 自定义注解处理器

在编译期间处理注解的一种方法是使用注解处理器（Annotation Processors）。注解处理器是一个工具，它在编译时扫描和处理源代码中的注解。它们通常用于生成额外的源代码、修改现有代码或验证代码约束等。Lombok 就是通过注解处理器实现的，它在编译期间生成 getter、setter 等方法。

要创建一个注解处理器，你需要遵循以下步骤：

1. 创建一个自定义注解：

```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.SOURCE)
public @interface CustomAnnotation {
}
```

注意，我们将保留策略设置为 `RetentionPolicy.SOURCE`，因为我们只需要在编译期间处理此注解。

2. 创建一个注解处理器：

创建一个类，继承 `javax.annotation.processing.AbstractProcessor` 类，并覆盖 `process` 方法。此方法将在编译期间处理指定的注解。

```java
import javax.annotation.processing.*;
import javax.lang.model.SourceVersion;
import javax.lang.model.element.Element;
import javax.lang.model.element.TypeElement;
import javax.tools.Diagnostic;
import java.util.Set;

@SupportedAnnotationTypes("com.example.CustomAnnotation")
@SupportedSourceVersion(SourceVersion.RELEASE_8)
public class CustomAnnotationProcessor extends AbstractProcessor {

    @Override
    public boolean process(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv) {
        for (Element element : roundEnv.getElementsAnnotatedWith(CustomAnnotation.class)) {
            processingEnv.getMessager().printMessage(Diagnostic.Kind.NOTE, "Found @CustomAnnotation at " + element);
            // 在这里处理注解，例如生成源代码、修改代码或验证代码约束等
        }
        return false;
    }
}
```

3. 注册注解处理器：

**在项目的 `resources/META-INF/services` 目录下**，创建一个名为 `javax.annotation.processing.Processor` 的文件。在该文件中，写入注解处理器的完全限定类名：

```
com.example.CustomAnnotationProcessor
```

4. 将注解应用于代码：

在项目的其他部分，使用自定义注解：

```java
@CustomAnnotation
public class MyClass {
}
```

现在，当你编译项目时，`CustomAnnotationProcessor` 将处理 `@CustomAnnotation` 注解。在 `process` 方法中，你可以实现任何操作，如生成源代码、修改代码或验证代码约束等。

注意：要使用注解处理器，你需要将它们添加到编译器的类路径中。对于 Maven 项目，你需要将注解处理器作为依赖添加到 `pom.xml` 文件中，并在 `maven-compiler-plugin` 中启用注解处理。对于 Gradle 项目，需要将注解处理器添加到 `annotationProcessor` 配置中。不同的构建工具可能需要不同的配置方式。

## 动态代理

### jdk动态代理

JDK 动态代理的原理是在运行时动态地生成一个代理类，该代理类实现了目标类的接口，并将方法调用转发到一个处理器（`InvocationHandler`）。处理器负责执行实际的代理逻辑，例如在目标方法执行前后添加日志、性能监控等功能。

以下是 JDK 动态代理的主要步骤：

1. 定义一个处理器（`InvocationHandler`）实现类。这个类需要实现 `java.lang.reflect.InvocationHandler` 接口，并重写 `invoke` 方法。`invoke` 方法负责处理代理类中的方法调用，并实现需要的代理逻辑。

```java
class MyInvocationHandler implements InvocationHandler {
    private Object target;

    public MyInvocationHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 在目标方法执行前执行的逻辑
        System.out.println("Before method");

        // 调用目标对象的方法
        Object result = method.invoke(target, args);

        // 在目标方法执行后执行的逻辑
        System.out.println("After method");

        return result;
    }
}
```

2. 使用 `java.lang.reflect.Proxy` 类的 `newProxyInstance` 方法动态地创建一个代理类实例。这个方法需要三个参数：

   - 类加载器（`ClassLoader`）：用于加载生成的代理类。
   - 代理类需要实现的接口列表：代理类将实现这些接口。
   - 处理器（`InvocationHandler`）实例：当代理类的方法被调用时，将调用处理器的 `invoke` 方法。

```java
MyInterface target = new MyInterfaceImpl();
InvocationHandler handler = new MyInvocationHandler(target);
MyInterface proxy = (MyInterface) Proxy.newProxyInstance(
    target.getClass().getClassLoader(),
    target.getClass().getInterfaces(),
    handler
);
```

在这个例子中，`proxy` 是一个动态生成的代理类实例，它实现了 `MyInterface` 接口。当 `proxy` 的方法被调用时，会转发到 `MyInvocationHandler` 的 `invoke` 方法。`invoke` 方法中可以实现需要的代理逻辑，例如在目标方法执行前后添加日志。

总之，JDK 动态代理的原理是在运行时动态地生成代理类，并将方法调用转发到处理器（`InvocationHandler`）。处理器负责实现代理逻辑。





## Object里面的方法

`java.lang.Object` 是 Java 中所有类的父类。当创建一个新的类时，如果没有显式地继承其他类，那么这个类将默认继承 `Object` 类。`Object` 类中的方法在任何 Java 类中都可以使用。以下是 `Object` 类中的一些主要方法及其作用：

1. `public String toString()`: 返回对象的字符串表示。通常需要在自定义类中覆盖此方法，以便为对象提供有意义的字符串表示。

2. `public boolean equals(Object obj)`: 比较两个对象是否相等。通常需要在自定义类中覆盖此方法，以便根据类的属性来判断对象是否相等。

3. `public int hashCode()`: 返回对象的哈希码值。当覆盖 `equals()` 方法时，通常也需要覆盖 `hashCode()` 方法，以便满足“相等的对象必须具有相等的哈希码”的约定。

4. `protected Object clone() throws CloneNotSupportedException`: 创建并返回当前对象的副本。**为了实现克隆功能，需要实现 `Cloneable` 接口并覆盖此方法。**

5. `public final Class<?> getClass()`: 返回对象的运行时类。此方法可用于获取对象的类信息，如类名、接口、父类等。

6. `protected void finalize() throws Throwable`: **当对象被垃圾回收器回收时，将调用此方法。在 Java 9 中，此方法已被弃用，因为使用 `finalize()` 方法可能导致性能问题和资源泄漏。建议使用其他清理资源的方法，如 `try-with-resources` 语句或 `AutoCloseable` 接口。**

7. `public final void wait() throws InterruptedException`: 使当前线程等待，直到其他线程调用此对象的 `notify()` 方法或 `notifyAll()` 方法。这个方法常用于多线程编程中的线程间同步。

8. `public final void notify()`: 唤醒在此对象监视器上等待的单个线程。这个方法也常用于多线程编程中的线程间同步。

9. `public final void notifyAll()`: 唤醒在此对象监视器上等待的所有线程。这个方法同样常用于多线程编程中的线程间同步。

在自定义类中，可以根据需要覆盖这些方法，以实现特定的功能和行为。
