---
title: Python编程快速上手 总结
date: 2023-3-4
---

> 编程是一项创造性任务

## 前言

> 程序开发要学会 **站在巨人的肩膀上** 。动手写代码前，先调研一番，看是否有现成的解决方案。 **切忌重复造轮子** ，浪费时间不说，可能代码质量还差，效果也不好。

这个是基于python 3.8 总结的

在 *Python* 中，一切皆对象，基本数据类型也是如此

## 第一部分 python 基础

### 基本运算符

> 这里介绍python独特的运算符

#### 算数运算符

|  操作符 | 操作 |
|  ---   |  --- |
| * | 数字相乘求积,字符串,列表这些跟整数相乘是复制 |
| ** | 指数 |
| / | 除法 |
| // | 除法取整,但是**结果的数据类型是两个操作数中表示范围最大的一个的数据类型** |
| + | 字符串,列表这些加法拼接,数字加法求和 |

> 整数如果在数值上与浮点数是相同的,用==比较时,他们就是相同的,不用管浮点数误差问题
>
> 记住python 没有 ++ --这种操作符

### 逻辑运算符

| 操作符 | 操作                         |
| ------ | ---------------------------- |
| and    | 两边表达式都为真才返回真     |
| or     | 两边表达式有一边为真就返回真 |
| not    | 返回表达式的相反情况         |

### 特殊运算符

| 操作符 | 操作                                 |
| ------ | ------------------------------------ |
| in     | 判断前面这个对象是否存在后面的对象中 |
| not in | 自然是in的相反                       |

三元运算符

```
flag = False
print( 1 if flag else 10)  # 如果flag 为 True则返回 1否则返回 10
```

只有0 空字符串 和 None 为False

### 常用函数

| 函数名                 | 操作                                   |
| ---------------------- | -------------------------------------- |
| str()                  | 将其他数据类型变成字符串               |
| int()                  | 将其他数据类型变成整数                 |
| float()                | 将其他数据类型变成浮点数               |
| list()                 | 将其他可迭代数据(字符串,元组)变成列表  |
| tuple()                | 将其他可迭代数据(字符串,列表)变成元组  |
| set()                  | 将其他可迭代数据(字符串,列表)变成集合  |
| range(start,stop,step) | 产生一个序列 [ start,stop), 步长为step |
|                        |                                        |
|                        |                                        |

### 代码块

> 代码块就是出于同一个块里面的代码,他们要么一起执行,要么都不执行

在python中 以缩进表示一个代码块, 相同缩进的且所有父代码都相同代码是处于同一个代码块的

```python
a = 10
b = 10
if a >= b:
    print(a)  # 代码块1
else:
    print(b)  # 代码块2
#虽然他们 有着相同的缩进,但是父代码不同
```

### 控制流语句

#### if

```python
if :
elif :
else :

```

#### while

```python
while true:
	
```

#### for

```python
for i in [1,2,3]
```

> 这个for 要特别注意,它和c++,java 这些里面的for不同,这里的for 好像只能用来遍历后面的数据,里面用的是迭代器

### 包和模块

#### 模块

一个以.py 结尾的文件就是一个模块,模块让你能够有逻辑地组织你的 Python 代码段，把相关的代码分配到一个模块里能让你的代码更好用，更易懂

模块需要注意的是 \_\_ name\_\_ 这个属性, 当我们执行的是这个模块的时候,它的值  是 \_\_ main\_\_ 如果是被导入的时候 那就是 模块名

##### 导入模块

import 模块名

import 用于导入某个模块

from  import 用于导入某个模块的某些东西

import  a.b as b = from a import b as b

上面都是绝对路径,还有相对路径的

import .a  导入当前模块下的a

import ..a  导入上层模块下的a

```python
import random as r
import random
from random import randint

print(r.randint(0,1))
print(random.randint(0,1))
print(randint(0,1))

```

当你导入模块的时候，Python解释器会把模块的代码编译成字节码，并放入 `__pycache__`文件夹中。这样以后再次运行的话，如果被调用的模块未发生改变，那就直接跳过编译这一步，直接去`__pycache__`文件夹中去运行相关的 *.pyc 文件，大大缩短了项目运行前的准备时间。

####  包

在早一点的 Python 版本（Python 3.3 之前）中，如果一个文件夹下有一个 **`__init__.py`** 文件，那我们就称之为包，英文名 Package。

在后来的 Python 版本（Python 3.3 开始）中，就没有这个要求了，**只要是文件夹就可以当做包**，我们称之为空间命名包，为做区分，我把上面那种包称之为 传统包。

今天这节里主要讲讲传统包的内容。

传统包里的 `__init__.py` 可以为空文件，但一定要有该文件，它是包的标志性文件，在需要情况下可以在里面进行一些包的初始化工作。

一个包里可以有多个模块，比如一个 demo 包包含`foo.py` 和 `bar.py`,那么在引用的时候就需要:

```python 
import demo.foo
import demo.bar
```

#### 库

Python 库是指一定功能的代码集合，通常认为他是一个完整的项目打包。

库->包->模块，是从大到小的层级关系！

- 库：一个库可能由多个包和模块组成
- 包：一个包可能由多个模块组成
- 模块：一堆函数、类、变量的集合

### 列表

列表就是一些数据的集合,他可以使用负数作为下标访问,也可以使用切片,s[a:b] = [s[a],...s[b-1]] ,这些切片都是浅拷贝出来的,字符串,元组也有这些特性

```python
s = [1,2,3]
s[-1] # 3
s[0:1] # [1]
s[0:-1] #[1,2]
s[:] # [1,2,3]
s[0:] # [1,2,3]
s[:1] # [1]
```

![image-20230305185214450](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230305185214450.png)

![image-20230305185233509](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230305185233509.png)

#### index方法

查找列表中的值,找到第一个位置并返回下标,没找到抛出ValueError异常

#### append/insert方法

append往列表末尾追加,insert指定位置添加

#### remove方法

删除第一个符合的数据,如果列表中不存在这个数据就会抛出ValueError

#### sort方法

对列表进行排序,我们也可以指定排序规则,还有通过reverse 参数控制是否逆向排序

### 元组

元组用()把数据包起来,而且如果数据只有一个的时候,我们必须以逗号结尾,不然python会以为我们是一个数据带了个括号而已

### 集合

自带去重,使用set() 创建空集合

### 字典

一个键对应一个值,跟c++里面的map一样,字典不是连续摆放键值对的,因此无法像列表那样使用切片

**创建空字典的方式是使用 {}**

#### keys()、values()和 items()方法

返回数据类型（分别是 dict_keys、dict_values 和 dict_items),这些方法返回的值不是真正的列表，它们不能被修改

#### get()方法

在访问一个键的值之前，检查该键是否存在于字典中，这很麻烦。好在，字典有一个 get()方法，它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值。

#### setdefault()方法

setdefault()方法提供了一种方式，在一行中完成这件事。传递给该方法的第一个参数，是要检查的键。第二个参数，是如果该键不存在时要设置的值。如果该键确实存在，方法就会返回键的值,**这个方法可以很好用来初始化数据**,但是啊我觉得直接这样更好, dicts['key'] = dicts.get('key',0)+1

### 字符串

字符串可以用单引号,双引号,三引号包裹,前两个没有什么区别,第三个可以用来表示注释,也可以换行写字符串,对于那些有很多行的字符串,我们可以使用三引号包裹,如果字符串里面有引号的话,需要使用转义字符 \\ 来转义,或者使用原始字符串的格式 r''



我们可以使用 in ,not in 精准匹配一个字符串是否包含另外一个字符串

| 方法            | 操作                                                         |
| --------------- | ------------------------------------------------------------ |
| upper()         | 将所有字母转成大写                                           |
| lower()         | 将所有字母转成小写                                           |
| isupper()       | 是否有字母且全部是大写                                       |
| islower         | 是否有字母且全部是小写                                       |
| isalpha()       | 是否包含字符且只有字符                                       |
| isalnum()       | 是否包含字符和数字且只有字符和数字                           |
| isdecimal()     | 是否包含数字且只有数字                                       |
| isspace()       | 是否包含空格,制表符,换行符,且只有这些字符                    |
| istitle()       | 是否所有单词都是开头大写,后面全部小写                        |
| startswith()    | 以某个字符串开头                                             |
| endswith()      | 以某个字符串结尾                                             |
| join()          | **以当前字符串为分割符,依次将可迭代序列生成新的字符串**      |
| split()         | 以某个字符串分割整个字符串,默认是空格,连续两个分割字符串出现的话会产生一个空串 |
| ljust(num,char) | 左对齐,字符不够使用给定字符(默认是空格)来补                  |
| rjust           | 同理                                                         |
| center          | 同理                                                         |
| strip()         | 去除两边空白字符,空格,制表符,换行符                          |
| l               |                                                              |



#### upper()、lower()、isupper()和 islower() 方法

可以将字符串变成大写或者小写,判断是否全部大写或者小写

isalnum() isdecimal() 

### 可变数据与不可变数据

我们得明白一件事,变量其实都是一个地址值,**他们指向了内存的一块区域,而这个可变与不可变指的是这块区域的数据**, 而对于这个变量的地址值,我们可以随便改变

对于列表,这块区域是可以变的,对于字符串,元组,这块区域是不可以变的

```python
a = (1,2,3) # 元组
a[0] = 1 # 错误 修改不可变区域的数据
a = (1,2,3,4) #正确,我们并没有修改一开始a指向区域的数据,我们只是修改了a的地址值,让a指向另外一片区域
```

### del语句

删除一个变量,删除后就不能再使用它了,但是在列表这样的中相当于移除它

### 多重赋值

```python
a = 10
b = 9
a,b = b,a

s = [1,2]
a,b = s
```

### copy模块

它包含了浅拷贝copy和深拷贝deepcopy两个函数

### 关于缩进

对于列表,元组这种数据定义的时候,缩进其实是没有用的,还有就是如果我们想把语句分成多行可以使用 \\ 这个字符来续行

```python
print("hello\
world")
```

### 漂亮打印pprint

如果列表,元组,字典里面数据较多或者相互嵌套的话,那么使用print打印出来的就比较丑,这个时候我们可以使用pprint 模块

![image-20230304165050060](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230304165050060.png)

![image-20230304165059827](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230304165059827.png)

对比一下吧,而且我们还可以使用它的pformat将其变成字符串格式

### pass

在 Python3.x 的时候 pass 可以写或不写。

python2.x：

```python
def function():
    # 空函数在Python2.x版本中pass是必须的
    pass
```

python3.x

```python
def function():
    # 在Python3.x的时候pass可以写或不写
    pass
```



### 函数

```python
def func(args):
	return
```

默认返回None

#### 参数问题

个人把参数问题分为两类:

* 定义的时候参数问题
* 传递的时候参数问题

在定义的时候有三种: 

##### 必选参数

```python
def func(a,b): # 这样定义的参数就叫必选参数
	pass
func(10,20)  # 这样传递的参数就是位置参数
func(10,b=30) # b =30 这样就是关键字参数
```

##### 默认参数

```python
def func(a,b=10):  # 必须在必选参数后面
	pass

```

##### 不定长参数

超出的**位置参数**当成元组放入argv中,超出的 关键字参数放入kwd 

```python
def func(*argv,**kwd):
	pass

```

##### 特殊参数

/ 和 \*  

/代表之前的参数只能用位置参数,* 代表之后的参数只能用关键字参数

![image-20230305190550055](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230305190550055.png)



要注意下面的规则:

1. **传递参数的时候**位置参数必须出现在关键字参数前面

2. 定义函数的时候 , **kwd这种参数必须放在\*argv这种参数前面,因为上一条规则,普通参数必须放在默认参数前面

3. 定义的时候*argv这中参数可以放在必选参数前面，但是在调用时，必选参数必须要指定参数名来传入，否则会报错

4. 不定长参数中的关键字参数不能跟函数定义参数名字相同,否则会冲突

#### 参数解析

比如说我们一个函数可以传递位置参数,我们可以解析列表进去,如果一个函数可以传递关键字参数,我们可以解析字典进去

```python
def func(a,b,c,d):
    
    print(a,b,c,d,sep="\n")

func(*[1,2],**{'c':10,'d':20})
```

这样确实可以省点事

### lambda表达式

第一个位置是参数,第二个是表达式

```python
lambda x, y: x+y  # 求和
lambda x, y: x if x < y else y # 比大小
func = lambda n:1 if n == 0 else n * func(n-1) # 递归
```

### 高阶函数

#### map(映射)

它是将可迭代对象的每一个数据都分别放入函数中,然后将函数的返回值变成一个map(可迭代对象)返回

![image-20230306155639537](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230306155639537.png)

```python
class map(Iterator[_S], Generic[_S]): # 我们发现他是可以迭代,也是生成器
```

第一个参数是一个函数,第二个参数是可变长迭代对象,返回的是一个map对象,他也是可以迭代的

```python
ll = map(lambda x:x**2,[1,2,3])
print(list(ll)) # [1,4,9]
ll = map(lambda x,y:x+y,[1,2,3],(4,5,6))
print(list(ll)) # [5,7,9]
```



#### filter(过滤)

![image-20230306160339383](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230306160339383.png)

![image-20230306160405245](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230306160405245.png)

```python
ll = filter(lambda x:x%2==0,[1,2,3])
print(list(ll)) # [2]
```

#### reduce(归约)

![image-20230306160903441](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230306160903441.png)

![image-20230306160818570](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230306160818570.png)

```python
import functools
res = functools.reduce(lambda x,y : x+y,[1,2,3,4,5])
print(res)  # 15
```

### 反射

这就是反射吧

1. 告诉别人，我是谁
2. 告诉别人，我能做什么

我们可以通过反射函数知道某个模块,某个类的一些信息

#### dir()

返回传递给它的任何对象的属性名称,是一个排好序的列表

![image-20230306162731170](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230306162731170.png)

#### type()

返回类型

#### hasattr()

![image-20230306162708633](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230306162708633.png)

使用 dir() 函数会返回一个对象的属性列表。

但是，有时我们只想测试一个或多个属性是否存在。如果对象具有我们正在考虑的属性，那么通常希望只检索该属性。这个任务可以由 hasattr() 来完成.

#### getattr()

使用 hasattr 获知了对象拥有某个属性后，可以搭配 getattr() 函数来获取其属性值。

#### id()

**id()** 函数返回对象的唯一标识符，标识符是一个整数。

#### isinstance()

使用 isinstance() 函数可以确定一个对象是否是某个特定类型或定制类的实例。

![image-20230306163223421](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230306163223421.png)



#### callable()

使用 callable 可以确定一个对象是否是可调用的，比如函数，类这些对象都是可以调用的对象。

#### 对于模块

#### \_\_doc\_\_

使用 `__doc__` 这个魔法方法，可以查询该模块的文档

#### \_\_name\_\_

始终是定义时的模块名；即使你使用import .. as 为它取了别名，或是赋值给了另一个变量名。

当前运行的文件的模块名字是 \_\_main\_\_ 如果这个模块不是被应用进来的时候,那就是文件名字

#### \_\_file\_\_

包含了该模块的文件路径。需要注意的是内建的模块没有这个属性，访问它会抛出异常！

#### \_\_dict\_\_

包含了模块里可用的属性名-属性的字典；也就是可以使用模块名.属性名访问的对象。

#### 对于类

#### \_\_doc\_\_

文档字符串。如果类没有文档，这个值是None。

#### \_\_name\_\_

始终是定义时的类名。

#### \_\_dict\_\_

包含了类里可用的属性名-属性的字典；也就是可以使用类名.属性名访问的对象。

#### \_\_module\_\_

包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象。

#### \_\_bases\_\_

直接父类对象的元组；但不包含继承树更上层的其他类，比如父类的父类。



### 作用域  和 命名空间

分为 **全局作用域 G**,**局部作用域 L**,**内建作用域B**,**闭包函数外的函数中E**

变量/函数 的查找顺序： L –> E –> G –>B

每个作用域都包含一个**命名空间**,我们在使用变量的时候会先在当前命名空间里面找有没有这个变量,如果没有会向外层找,我们在给变量赋值的时候,如果没有使用**global,nonlocal** 这些关键字向外面引入变量,那么将会在自己的命名空间里面创建这么一个变量

#### 全局与局部



```python
def func():
    a = 10  # 局部
a = 20  # 全局
func()
print(a)  # 输出20
```

我们发现在func里面对a赋值其实是在局部作用域里面创建了一个a,而不是对全局的a做修改,那么如何在函数里面修改全局变量呢?

#### global 关键字

引入全局作用域里面的变量,如果不存在,当我们对这个变量赋值的时候,则会在全局作用于的命名空间里面定义这么一个变量

```python
def func():
     b = 10  # 不能再出现a的使用
     global a  # 如果不使用这条语句,下面这条语句将变成 定义一个局部变量
     a = 10
func()
print(a)  # 10
```

> 在函数里面,我们不能再global语句前面出现任何关于使用global指定变量的语句

**另外还需要注意的点,如果局部变量跟全局变量重名了,在局部变量声明前,是不能使用这个变量名字的,会被看做未定义**,比如这样

```python
def func():
   print(a)  # 这里会报错
   a = 10
a = 20
func()
print(a)
```

#### nonlocal关键字

**这个呢是用来引入外层命名空间里面的变量的,而不是全局**,如果不存在,则会报错

```python
def func1():
   
    def func2():
        
        nonlocal a  
        a = 10
     # 这个其实也是E作用域相对于func2里面来说
    a = 20   # 如果不定义 那么在 func2 里面会报错
    func2()
    print(a)  # 输出10
    
func1()
```

#### 变量集合

在Python中，有两个内建函数，你可能用不到，但是需要掌握它们。

- globals() ：以dict的方式存储所有全局变量/函数
- locals()：以dict的方式存储所有局部变量/函数

#### 总结

如果我们仅仅使用变量而不赋值,那么会从当前作用域一层一层向外找,**而且外层的声明语句必须在调用这个作用域的时候的前面**,如果我们对变量进行赋值了, 如果没有特殊关键字修饰,那么就是当前作用域定义,如果有global修饰,那么就是修改全局作用域中的变量,或者是赋值(全局可以不存在这个变量),如果有nonlocal修饰,那么就是修改外面一层作用域的变量而且外层作用域必须先定义好这个变量

### 闭包

在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。

```
def deco():
    name = "MING"
    def wrapper():
        print(name)
    return wrapper
```



### 异常处理

```python
try:
	代码
except Exception as e:  # 建议这样做,才能得到异常对象,如果不加 as 的话就是异常类
	处理
else:
    没发生异常执行
finally:
    都会执行的代码
raise  # 向上抛出异常
```

### 类和对象

感觉python的类和对象整的就很.....,不知道咋说,感受一下吧,

```python
class Car:  # 也可以class Car()
    
    def __init__(self) -> None:   # 初始化函数,也就是构造函数吧
        self.price = 10  # 这里必须用self.xxx 的格式,不然就不是这个对象的属性,还记的作用域跟命名空间么,但是这里不能用nonlocal
        self.color = 'red'
    
car1 = Car()
car1.number = '10000'   # 这样的话 number 也属于 car1 的属性了
print(car1)
```

当我们使用对象名.方法名的时候相当于 类名.方法名(对象名)  所以方法的第一个参数就是self,也可以取别的名字,当我们使用类名.方法名的时候,就相当于普通函数

#### 类属性

```Python

class User:
    a = 10        
user = User()
user.a = 20
print(user.a)
print(User.a)
```

类属性存在与类的dict里面,  而不在实例的dict里面

#### 静态方法 类方法 实例方法

静态方法和类方法必须使用@staticmethod   @classmethod  两个装饰器装饰才行,不然一律当做实例方法

这三个东西真的比较混乱,我们从调用上来理解

```python
class User:
    def test(self):
        print(self)
    @staticmethod
    def test1(a):
        print(a)
    @classmethod
    def test2(a):
        print(a)
    
user = User()

# 实例调用的时候,第一个参数传递的是自己
# 类名调用的时候就是普通函数调用
user.test()  
User.test(user)  

# 两种方式都是普通函数调用
user.test1(1)
User.test1(1)

#两种方式都会将类当成第一个参数传进去
user.test2()
User.test2()
```

三种方法声明要注意:  静态方法必须使用@staticmethod装饰,然后参数可以定义也可以不定义, 类方法必须使用@classmethod装饰,必须定义一个参数,这个参数就是类本身, 实例方法必须要定义一个参数(除非你不通过实例调用这个方法),这个参数就是实例本身

#### 私有变量和方法

python中其实并没有提供这种功能,我们可以在类外调用任何变量和方法,这个只是一种规范罢了

##### 单前导下划线 \_var

下划线前缀的含义是告知其他程序员：**以单个下划线开头的变量或方法仅供内部使用**。

##### 双前导下划线 \_\_var

双下划线前缀会导致Python解释器**重写属性名称**，以避免子类中的命名冲突。

这也叫做**名称修饰(name mangling)** - 解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。

```python
class User:
    def __init__(self) -> None:
        self.__name = '10'
    def __func(self):
        pass
    def getage(self):
        return self.__name  
print(User().__dict__)  #{'_User__name': '10'}
print(User.__dict__)  # '_User__func': <function User.__func at 0x0000027AF68C2820>
print(User().getage())  #  这样是没有问题的
print(User().__name)  # 这样会报错
```

我们发现,名字被重写了,变成了 \_类名变量名 的格式了,  我们在内部可以直接使用\_\_name这样的形式,而在外部则不行,这样是不是也做到了一定上的私有化呢?

#### 继承

##### 单继承

```python
# 父类定义
class People:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} 说: 我{self.age}岁。")
class Student(People):
    def __init__(self, name, age, weight, grade):
        # 调用父类的实例化方法,这里必须带上self
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 重写父类的speak方法
    def speak(self):
        People.speak(self)
        print(f"我在读{self.grade}")
```

子类的属性和方法会重写父类的属性和方法

#### 多继承

```
class 子类(父类1, 父类2, 父类3...):
```

如果多个父类中有相同的方法跟属性,访问的时候优先选择左边的

![image-20230307171808747](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307171808747.png)

![image-20230307171850020](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307171850020.png)

从左到右再深度选择

![image-20230307171918818](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307171918818.png)

#### super

这个玩意也有很多坑,这个东西是用来调用父类的属性跟方法,但是如果父类中的方法也使用了super 调用方法的话,那就得注意了,它不是简简单单的调用父类的父类的方法,而是去_mro_中找下一个父类的顺序

```python
class Base:
    def __init__(self):
        print('Base.__init__')
        
    def hello(self):
        print("Base")
    
        
class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')
        
    def hello(self):
        print("A")
        
        
class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')
        
    def hello(self):
        print("B")
        
        
class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')
        self.hello()
C()
# 输出
# Base.__init__
# B.__init__
# A.__init__
# C.__init__
# A
        
```

按理来说是不是应该输出 

```
Base.__init__
A.__init__
C.__init__
A
```

有没有发现多输出了B的,这就说明了如果父类方法也使用了super,那么下一个找的是mro链里面的方法

#### property装饰器

使用property去装饰类里面的一个方法的时候,会将其变成属性,当我们访问这个属性的时候就会调用里面的方法,(这个和vue的计算属性很像),如果直接对对象里面的其他属性赋值的话,那么就不能对其进行约束和检查,如果我们采用这个property修饰的属性去赋值,那么就能够实现检查和约束

```python
class User:
    def __init__(self,age) -> None:
        self.age = age

    # 将方法变成属性
    @property 
    def age(self):
        return self._age
    # 检查值是否合法
    @age.setter
    def age(self,age):
        if age < 0:
            raise Exception("age invalid")
        self._age = age

    
user = User(10)
# 不合法,会抛出异常
user = User(-10)
```

我们打印User.\_\_dict\_\_ 会输出 'age': <property object at 0x0000022BB2FEBF90>  他变成了property的对象了

- 当你读取属性值时，会进入被 `property` 装饰的函数。
- 当你对属性进行赋值时，会进入被 `@xx.setter` 装饰的函数。
- 两个装饰器，一定是 `@property` 在前面，而 `@xx.setter` 在后

#### 类的魔法方法

##### 构造方法

![image-20230307180058571](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180058571.png)

##### 比较运算符

![image-20230307180040473](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180040473.png)

##### 一元操作符

![image-20230307180154965](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180154965.png)

##### 算数操作符

![image-20230307180229621](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180229621.png)

![image-20230307180258476](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180258476.png)

![image-20230307180447324](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180447324.png)

##### 增强赋值运算符

![image-20230307180538110](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180538110.png)

##### 类型转换运算符

![image-20230307180601912](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180601912.png)

##### 类的表示

![image-20230307180721780](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180721780.png)

![image-20230307180802074](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307180802074.png)

##### 访问控制

![image-20230307181404626](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307181404626.png)

![image-20230307181131165](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307181131165.png)

##### 自定义序列

![image-20230307181441101](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307181441101.png)

##### 反射

![image-20230307181630304](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307181630304.png)

##### 可调用对象

![image-20230307181648695](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307181648695.png)

##### 上下文管理器

![image-20230307181712884](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307181712884.png)

##### 属性描述符

![image-20230308180510390](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230308180510390.png)

> 千万要注意,它一定要属于某个类的属性才能使用,是对象属性都不行,而且必须得是被对象或者类去用点.去访问或者修改才会触发set和get函数,使用dict 是没有用的

这里很有必要讲一下这个东西,它能够限制和检查类里面的属性,跟\_\_setattr\_\_ 这样差不多,不过它相当于另外一种数据类型,而且如果使用\_\_setattr\_\_ 来做检查与限制会使得代码很冗余,而属性描述符就很简单了,看下面这个代码,基本上所有的分数都可以用这个描述符去限制,如果用\_\_setattr\_\_ 来的话,那岂不是每个分数都要判断一次,而且他可以做到每一次修改都能检查跟限制

```python
class Score:
    def __init__(self,score) -> None:
        self.score = score
    def __get__(self,instance,owner):
        print("__get__",instance,owner,sep="\n")
        return self.score
    def __set__(self,instance,value):
        print("__set__")
        if value < 0 or value > 100:
            raise Exception("value invalid")
        self.score = value

class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

student = Student("dd",1,2,3)
student.english
```

这里要注意一下,我们在初始化函数里面明明是对实例属性赋值,但是由于属性描述符的原因,所以赋值变成对属性描述符修饰的属性赋值,而name则不受影响,所以我们打印student.\_\_dict\_\_的时候只能看到name

###### 数据描述符与非数据描述符

如果只有\_\_get\_\_  那么就是非数据描述符,如果有 \_\_set\_\_和\_\_get\_\_两个就是数据描述符,**数据描述符和非数据描述符的区别在于：通过实例修改与类属性同名的描述符时,数据描述符是修改类属性,而非数据描述符则是修改或者创建这么一个实例属性**。

##### **拷贝**

![image-20230307181840529](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230307181840529.png)

> 这些魔法方法,其实都是为了方便或者提供一种好的办法给我们,我们可以通过这些魔法方法让我们的类能够支持更多的操作,比如加法,减法,支持内建函数这些,这些方法也不是必选的,你需要什么功能,你就去实现什么方法

#### 元类

**类是用来创建对象的**,**元类是用来创建类的**  因此类时元类的对象

```python
User = type("User",(),{"name":"djm"})

user = User()

print(user.name)
print(user.__class__) # 打印出创建自己的类  User
print(User.__class__) # 打印出创建自己的类  type
```

**一个类要具有创建其他类的本领的话就必须继承type**

```python
class test(type):
    def __new__(cls,*args,**kwd):
        print("in test")
        return super().__new__(cls,*args,**kwd)

class User(metaclass = test):
    pass
```

上面我们说到,User类时test元类的一个实例,因此必然会走test的 new 方法,因此 会输出in test 

既然这样我们是不是可以在创建类时候自定义一些属性,还有是在类在创建对象的时候往对象身上添加一些属性(利用 call函数)

```python
class test(type):
    def __new__(cls,*args,**kwd):
        
        obj =  super().__new__(cls,*args,**kwd) 
        obj.age = 10 # 往User类上添加一些属性
        return obj
    def __call__(self, *args, **kwds) :
        obj = super().__call__(*args, **kwds)
        obj.name = 'hello world'  # 往User 实例对象上添加属性
        return obj
    

class User(metaclass = test):
   pass
```

所以这不就正符合框架的做法了么,毕竟通过元类我们能够动态的做很多事,而我们平常基本上是用不到元类的



### 迭代器

python的列表,元组,集合,字典这些容器都提供了迭代器,所以我们能够使用for in 来循环遍历,如果我们想让for in 来遍历我们自己的对象,我们需要在类中定义 \_\_next__  和 \_\_ iter__ 两个方法

> 如果只是为了实现for in 的话  实现 \_\_getitem\_\_ 这个方法就行

我们可以使用 iter 方法获得对象的迭代器,然后使用next遍历数据,当next 抛出StopIteration 异常就代表迭代结束

```python
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()

for x in (myclass):
  print(x)

it = iter(myclass)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
```



### 生成器

生成器的出现（Python 2.2 +），实现了延时计算，从而缓解了在大量数据下内存消耗过猛的问题。

#### 创建生成器

第一种方式

```python
[i for i in range(5)] # [0,1,2,3,4]
gen = (i for i in range(5)) # 注意和列表推导式的区别哦,这个返回的是一个生成器对象
```

第二种方式

使用yield

`yield` 是什么东西呢? 它相当于我们函数里的 return，但与 return 又有所不同。

- 当一个函数运行到 yield 后，函数的运行会暂停，并且会把 yield 后的值返回出去。
- 若 yield 没有接任何值，则返回 None
- yield 虽然返回了，但是函数并没有结束,等到下一次继续运行的时候会接着yield后面这里运行

#### 生成器的使用

可以使用for in 循环跟 next函数,这个就跟迭代器的使用差不多了

还可以使用send方法

```python
def func():
    i = 0
    while i<5:
        b = yield i
        if b == None:
            return 
        i += b
    
gen = func()

print(gen.send(None))
print(gen.send(1))

```

send方法可以传递参数,作为 yield返回值,而且第一次传递参数必须是None

当我们第一次执行send函数的时候,是直接停在了yield那里,那么这个返回值当然不是它设置,而是第二次继续send的时候将传递来的参数当做返回值, 就是这么设计的

#### 生成器异常

当我们的函数执行完后,会自动抛出一个停止异常

```python
def func(a):
    print("前面")
    yield a
    print("后面")
    
gen = func(10)

gen.send(None)
gen.send(None) # 这里会出一个异常,其实也是为了告诉别的使用者,生成器已经执行完了
```

#### 生成器的函数返回值

```python
def func():
    yield 10
    return 10,20

gen = func()
next(gen)
try:
    next(gen)
except StopIteration as s:
    print(s.value)  # (10,20)
```



#### 生成器常用方法

send(val) :  传递val作为 yield 语句的返回值

 throw: 传递异常给生成器里面的yield语句

```python
def func():
    print("前面")
    try:
        yield lambda x:1/x
    except Exception:
        print("出现异常")  
    print("后面")
    
gen = func()
div = gen.send(None)


try:
    print(div(1))
    print(div(0))  # 这里会出现异常
except Exception:
    try:
        gen.throw(Exception) # 我们将异常交给生成器内部去处理
    except Exception:   # 这里是为了处理stop那个异常
        pass 

```

#### yield from 

这个语句后面要跟一个可迭代对象(自然就包括生成器)  然后调用这个生成器就能一次遍历这个对象

```python
def func():
    a = [1,2,3]
    yield from  a  #等价于 for i in a: yield a

f = func()

print(next(f))
print(next(f))
print(next(f))

```

我们来看一下yield from 的参考代码吧,看看它干了些什么

```python
"""
_i：子生成器，同时也是一个迭代器
_y：子生成器生产的值
_r：yield from 表达式最终的值
_s：调用方通过send()发送的值
_e：异常对象
"""

_i = iter(EXPR)

try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value

else:
    while 1:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break
RESULT = _r
```

可以发现,它帮我们做了很多的异常处理

### 上下文管理器

#### 什么是上下文管理器

```python
with open("test.file") as f:
	f.readline()
```

1. 上下文表达式：`with open('test.txt') as file:`
2. 上下文管理器：`open('test.txt')`
3. `file` 不是上下文管理器，应该是资源对象

有没有发现,我们不需要自己去关闭文件

#### 有什么好处?

1. 可以以一种更加优雅的方式，操作（创建/获取/释放）资源，如文件操作、数据库连接；
2. 可以以一种更加优雅的方式，处理异常；

#### 如何编写上下文管理器

需要定义\_\_enter\_\_,\_\_exit\_\_这两个方法,

```python
class Resource:
    def __enter__(self):
        print("====enter=====")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('===close resource connection===')
        return True   # 这里如果不返回True的话,产生的异常就会接着往上面抛

    def operator(self):
        1/0

with Resource() as f:
    pass
```

运行之后,发现并没有报错

#### 使用contextlib

这个可以只使用一个函数就可以了,不需要重新多写一个类

```python
import contextlib

@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    try:
        yield file_handler
    except Exception as exc:
        # deal with exception
        print('the exception was thrown')
    finally:
        print('close file:', file_name, 'in __exit__')
        file_handler.close()

        return

with open_func('/Users/MING/mytest.txt') as file_in:
    for line in file_in:
        1/0
        print(line)
```

#### 自己实现contextlib

我们要明白这个with 的用法, with 后面的表达式的返回值必须是上下文管理器,也就是必须有 exit 和 enter 两个方法的对象, 然后调用它的enter方法得到返回值,就是资源对象, 等到结束后就执行exit方法,

```python 
class context:

    def __init__(self,func) -> None:
        self.func = func  # 保存好函数
    def __call__(self, *args, **kwds):
        self.args = args
        self.kwds = kwds
        return  self   # 这里要返回自己,但是要保存好参数信息
    def __enter__(self):
       self.handler = self.func(*self.args,**self.kwds)  # 执行函数得到生成器
       return next(self.handler)  # 返回资源对象
    
    def __exit__(self, exc_type, exc_val, exc_tb):

        
        try:
            if exc_type != None:
                self.handler.throw(exc_type)  # 如果有异常,就将异常交给生成器内部去处理,因为这个生成器肯定 是使用者自己写的,而这个上下文管理器是已经封装好的
            else:
                self.handler.send() # 将异常
        except StopIteration:
            pass
        
        return True

def func2(a):
    print(a)

@context
def func():
    print("__enter__")
    try:
        yield func2
    except Exception:
        print("产生异常")
    print("__exit__")

with func() as f:
    f(20)
    1/0
    
```



### 装饰器

装饰器就像代理一样,在不改变原先的代码的情况下,对其进行增强,它的返回也是一个函数对象,这样我们就能够节省很多代码,减少耦合

#### 普通装饰器

```python
import time

def testtime(func):
    def wrapper(*args,**kwd):
        start = time.time()
        result = func(*args,**kwd)
        end = time.time()
        print(func.__name__+"用时"+str((end-start)) +"s")
        return result
    return wrapper

@testtime
def test():
    j = 0
    while j<1000000000:
        j = j+1
test() # 等价于 testtime(test)()
```

#### 带参数的函数装饰器

上面这种普通的装饰器只能执行固定的逻辑,我们并不能对其传递参数

```python
import time

def delay(ns):
    def wrapper(func):
        def wrapper2(*argv,**kwd):
            time.sleep(ns)
            result = func(*argv,**kwd)
            return result
        return wrapper2
    return wrapper

@delay(1)
def sayhello():
    print("hello")

sayhello()   # 等价于  delay(1)(sayhello)()
delay(1)(sayhello)()
```

比如这个带参数的装饰器,我们可以给定延迟时间执行

#### 不带参数的类装饰器

上面这些都是函数装饰器,我们还可以用类来做装饰器,用类做装饰器必须实现两个方法,一个是\_\_init\_\_(用于传递被装饰函数)和 \_\_call\_\_(用来实现装饰逻辑)

```python
import time

class testtime:
    def __init__(self,func) -> None:
        self.func = func
    def __call__(self, *args, **kwds):
        start = time.time()
        result = self.func(*args,**kwds)
        end = time.time()
        print(self.func.__name__+"用时"+str((end-start)) +"s")
        return result


@testtime
def test():
    j = 0
    while j<1000000:
        j = j+1
test() # testtime(test).__call__() == testtime(test)()
```

#### 带参数的类装饰器

这个与不带参数的类装饰器有很大的变化 \_\_init\_\_(用于传递参数)和 \_\_call\_\_(用来接收被装饰函数)

```python
import time

class delay:
    def __init__(self,ns) -> None:
        self.ns = ns
    def __call__(self, func):
        def wrapper2(*argv,**kwd):
            time.sleep(self.ns)
            result = func(*argv,**kwd)
            return result
        return wrapper2
    

@delay(1)
def sayhello():
    print("hello")

sayhello()   # 等价于  delay(1).__call__(sayhello)() == delay(1)(sayhello)()
delay(1)(sayhello)()
```

#### 其他装饰器

* 类方法
* 实例方法
* 静态方法

#### 总结

有没有发现其实就只有两种装饰器  一种带参数,一种不带参数   最终使用格式分别为 A(P)(B)() 和 A(B)()  A代表装饰器,P代表参数,B代表被装饰的东西(**可以是类**,也可以是函数)  ,**如果修饰的是类那么就是装饰类创建对象的时候**

**而且 被修饰的东西都变成参数被传递到装饰器里面去了**,这个特别重要,后面要用到

### 并发编程

#### 多线程的使用

创建多线程的两种方式

> 两种方式各有千秋,第一个简单,第二个可以自定义很多内容

* 使用Thread 类 创建线程
* 继承Thead 类 重写run 方法

```python
import time
from threading import Thread

# 自定义线程函数。
def target(name="Python"):
    for i in range(2):
        print("hello", name)
        time.sleep(1)

# 创建线程01，不指定参数
thread_01 = Thread(target=target)
# 启动线程01
thread_01.start()


# 创建线程02，指定参数，注意逗号
thread_02 = Thread(target=target, args=("MING",))
# 启动线程02
thread_02.start()
```



```python
import time
from threading import Thread

class MyThread(Thread):
    def __init__(self, type="Python"):
        # 注意：super().__init__() 必须写
        # 且最好写在第一行
        super().__init__()
        self.type=type

    def run(self):
        for i in range(2):
            print("hello", self.type)
            time.sleep(1)

if __name__ == '__main__':
    # 创建线程01，不指定参数
    thread_01 = MyThread()
    # 创建线程02，指定参数
    thread_02 = MyThread("MING")

    thread_01.start()
    thread_02.start()
```

#### 锁机制

##### 互斥锁

```python
import threading

# 生成锁对象，全局唯一
lock = threading.Lock()

# 获取锁。未获取到会阻塞程序，直到获取到锁才会往下执行
lock.acquire()

# 释放锁，归还锁，其他人可以拿去用了
lock.release()
```

推荐使用 with lock

##### 可重入锁

```python
import threading

def main():
    n = 0
    # 生成可重入锁对象
    lock = threading.RLock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)

t1 = threading.Thread(target=main)
t1.start()
```

##### 全局锁GIL

> 在python中多个线程其实并不是并行,而是并发,交替运行

什么是GIL呢？ >任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

#### 线程通信

##### Event

```python
# 重置event，使得所有该event事件都处于待命状态
event.clear()

# 等待接收event的指令，决定是否阻塞程序执行
event.wait()

# 发送event指令，使所有设置该event事件的线程执行
event.set()
```

```python
from threading import Thread
from threading import Event
from threading import Lock
import time

event = Event()  
rank = 0
lock = Lock()

def run(name):

    global rank
    print(f"我是{name},我已经准备好了")

    # 等待发出枪声
    event.wait()
    # 开始竞争
    lock.acquire()
    rank += 1
    print(f"第{rank}名:{name}")
    lock.release()
    
event.clear()
runners = [Thread(target=run,args=[i]) for i in range(5)]
[runner.start() for runner in runners]

print("各就位")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print("开始跑")
event.set()
```

上面这个代码是5名选手参加跑步比赛,用event来控制统一开始跑, lock来模拟速度,谁先抢到谁排名高

##### condition

```python
cond = threading.Condition()

# 类似lock.acquire() 抢占锁
cond.acquire()

# 类似lock.release() 释放锁
cond.release()

# 等待指定触发，同时会释放对锁的获取,直到被notify才重新竞争这个琐。必须得先拥有锁也就是acquire
cond.wait()

# 发送指定，触发执行
cond.notify()
```

##### Queue

```python
from queue import Queue
# maxsize默认为0，不受限
# 一旦>0，而消息数又达到限制，q.put()也将阻塞
q = Queue(maxsize=0)

# 默认阻塞程序，等待队列消息，可设置超时时间
q.get(block=True, timeout=None)

# 发送消息：默认会阻塞程序至队列中有空闲位置放入数据
q.put(item, block=True, timeout=None)

# 等待所有的消息都被消费完
q.join()


# 通知队列任务处理已经完成，当所有任务都处理完成时，join() 阻塞将会解除
q.task_done()
```

#### 信息隔离

就是每个线程来的时候,去找他们自己对应的字典信息,我简略的实现一下就知道了,每个线程都有一个自己的字典域

```python
from threading import Thread,currentThread


class local1:
   def __getattribute__(self, __name: str) :
      if __name == "__dict__":
         object.__getattribute__(self,__name).setdefault(currentThread(),{})
         return object.__getattribute__(self,__name)[currentThread()]
      else:
         return self.__dict__[__name]

   def __setattr__(self, __name, __value):
      self.__dict__[__name] = __value
      
       
n2 = local1()
n2.name = "main"
n2.t = 10
def func(name):
   n2.name = name
   print(n2.__dict__)

[Thread(target=func,args=["thread"+str(i)]).start() for i in range(3)]


print(n2.__dict__)
```

![image-20230312185501172](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230312185501172.png)

#### 线程池

在使用多线程处理任务时也不是线程越多越好，由于在切换线程的时候，需要切换上下文环境，依然会造成cpu的大量开销。还有就是创建销毁线程也会消耗资源,为解决这个问题，线程池的概念被提出来了。预先创建好一个合理数量的线程池，让过来的任务立刻能够使用，就形成了线程池。

在Python3中，创建线程池是通过`concurrent.futures`函数库中的`ThreadPoolExecutor`类来实现的。

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(5)

def func():
    for i in range(10):
        print( f"{threading.get_ident()} : {i} " )
        time.sleep(1)
for i in range(10):
    pool.submit(func)

```

使用with 这样的方式更加优雅, submit 之后有一个返回值,  我们可以调用它的result 方法得到结果  但是这个方法是阻塞的,除非我们就是要现在得到结果,否则就将这个句柄保存起来,等到后面再得到结果



```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func():
    for i in range(10):
        print( f"{threading.get_ident()} : {i} " )
        time.sleep(1)
    return threading.get_ident()
with ThreadPoolExecutor(5) as pool:
    handlers = [pool.submit(func) for i in range(10)]
    res = [handler.result() for handler in handlers]
    dicts = {}
    dict
    for r in res:
        dicts[r] = dicts.get(r,0) + 1
    for k,v in dicts.items():
        print(f"{k} 执行了 {v}的函数")

```

#### 异步io asyncio框架

##### 协程

怎么去理解协程呢, 拿线程去对比一下吧, 如果我们有一个网络请求,需要1s钟才能得到响应, 如果是线程的话,它会一直在那等着,如果是协程,我们可以让CPU去干别的事情

协程的实现就是依靠生成器

##### 创建一个协程

只要在函数声明的前面用async声明就行了

```python
import asyncio
import time

async def request():
    await asyncio.sleep(1)
print(request())  # <coroutine object request at 0x000001F8FAE163C0>
```

##### 概念

在了解`asyncio`的使用方法前，首先有必要先介绍一下，这几个贯穿始终的概念。

- `event_loop 事件循环`：程序开启一个无限的循环，程序员会把一些函数（协程）注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
- `coroutine 协程`：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
- `future 对象`： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
- `task 任务`：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类，它将 coroutine 和 Future 联系在一起，将 coroutine 封装成一个 Future 对象。
- `async/await 关键字`：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield。

> async里面不能使用 yield ,await 也必须在async里面使用

##### 协程的并发

协程的并发其实是需要异步函数的支持,如果不是异步函数的话,协程是不能并发的,我们来对比一下

不支持异步的函数

```python
import asyncio
import time

async def request():
    time.sleep(1) # 不支持异步
    

async def main():
    task1 = request()
    task2 = request()

    task1 = asyncio.create_task(task1)
    task2 = asyncio.create_task(task2)

    await task1
    await task2

start = time.time()
asyncio.run(main())
end = time.time()
print(f"一共运行{end-start:.2f}s") # 2s
```

支持异步的函数

```python
import asyncio
import time

async def request():
    await asyncio.sleep(1)  # 这个是支持异步的
    

async def main():
    task1 = request()
    task2 = request()

    task1 = asyncio.create_task(task1)
    task2 = asyncio.create_task(task2)

    await task1
    await task2

start = time.time()
asyncio.run(main())
end = time.time()
print(f"一共运行{end-start:.2f}s")  # 1s

```



## 第二部分 自动化

### 正则表达式

> 关于什么是正则表达式,我已经在我的另外一篇博客里面介绍清楚了,这里只做关于python如何使用正则表达式的总结

python的正则表达式的使用有两种:

第一种就是 直接使用 re 模块里面的函数 比如 re.search(pattern,string,flags) re.match() re.findall() ... 

第二种就是 使用re.compile(pattern,flags)  得到一个对象,然后调用这个对象的search(string),match findall 方法

第一种呢,方便我们一次性使用,第二种方便一个匹配模式多次使用

#### search方法

搜索第一个匹配的字符串,并且返回包含这个字符串的匹配对象

#### match方法

从开头开始匹配,如果没有匹配成功,则不会继续匹配

#### findall方法

**返回全部匹配的字符串的所有分组(0分组除外,如果只有0分组的话就必须包含0分组)**,并且都放在列表中返回

#### finditer方法

匹配所有字符串,而且**我们可以迭代遍历所有的匹配对象**

四个方法总结一下吧:

如果我们只是想看某个字符串是否包含这个模式,我们可以使用search

如果我们要看从开头是否匹配,使用match

如果只需要得到所有匹配结果的分组,使用findall

如果要获得所有的匹配字符串,还要获得所有的匹配字符串的分组,使用finditer

### 读写文件

## 好用的功能

### **格式化字符串**

1. 通过字符串前加f/F  然后直接引用变量

   ```python
   a = 10
   s = f'i have {a:-3} apples'
   print(s)
   ```

2. 通过字符串的format方法

   ```python
   print('{:-3} apples'.format(10)) # 左对齐三位格式
   ```

   ![image-20230305204838893](../../img/Python编程快速上手-让繁琐工作自动化assets/image-20230305204838893.png)

### 不一样的作用域

在python中,貌似对这个代码块作用域不太敏感

```python
if 1 == 1:
    a = 10
print(a)  # 输出10
```

如果在c++和 java中,这个代码肯定会报错,我去,那这样也太爽了

### \_\_call\_\_方法

a.\_\_call\_\_ () == a()  这么一来,我感觉函数跟类其实也没有什么区别

### type返回值

type的返回值就是一个类,他也是一个对象,因此我们是不是可以根据某个数据直接造出跟它一样类型的对象

```python
def getobj(obj):
    return type(obj)()
print(getobj(111))
print(getobj("111"))
print(getobj([]))
print(getobj({}))
```



## 额外补充

### 可变对象与不可变对象

我们可以通过id()得到一个整数值,它代表唯一的一个对象,我们也可以把它理解成地址

可变对象就是我们可以修改对象里面的内容,不可变对象是不可以修改里面的内容的

```python
# 可变对象
l = [1,2,3]
print(id(l),sep='\n')
l += [10]
print(id(l),sep='\n')

# 不可变对象
a = 1
print(id(a),sep='\n')
a += 1
print(id(a),sep='\n')
# 2775197888320  
# 2775197888320
# 140721313420960
# 140721313420992
```

l += [10] 其实调用的是 \_\_add\_\_ 方法,它里面只是将10添加进去然后返回自己,所以地址值肯定没有变,而 a += 1 是返回了一个新的对象,所以地址值肯定变了, 所以对于这个所谓的可变对象与不可变对象,只是我们取决于我们在这些方法里面返回什么罢了,还有就是不可变对象可以通过 \_\_setattr\_\_里面抛出异常禁止我们设置值

```python
class Score:
    def __init__(self) -> None:
        self.score = 10
    def __setattr__(self, __name: str, __value) -> None:
        raise Exception("不允许操作")
s = Score()
s.score = 1000
```

### 对象属性访问和创建的规则

* 当我们对一个实例属性进行访问时，Python 会按 `obj.__dict__` → `type(obj).__dict__` → `type(obj)的父类.__dict__` 顺序进行查找

* 当我们对一个实例属性,**跟类属性不重名,或者类属性不是一个数据描述符**,进行赋值的时候,如果obj.\_\_dict\_\_ 里面不存在,那么就创建,如果存在则修改
* 当我们对一个实例属性,**跟类属性重名,而且类属性是一个数据描述符**,进行赋值的时候, 一定是按照这个顺序`type(obj).__dict__` → `type(obj)的父类.__dict__` 去修改数据

### property实现原理

装饰器  +  属性描述符  

我们好好想想这三个东西的功能:  property是将方法当成属性访问或者赋值,而且只要一访问就会执行这个方法并且得到返回值, 装饰器,能够增强函数的功能,  **把函数当做参数传递到装饰器里面**,属性描述符  当通过类或者实例点.属性名字的时候就会执行里面的 get set 方法

如果我们设计一个装饰器类,在init方法中保存修饰函数,它又正好是属性描述符,在get 和 set 方法里面执行对应的函数,用这个装饰器去修饰方法,那是不是就做到了通过访问属性名就能代替方法了

先看一个简单的例子吧

```python
class testfunc:
    def __init__(self,func) -> None:
        self.func = func
    def __get__(self,instance,owner):
        return self.func(instance)
class test:
    def __init__(self) -> None:
        self._age = 18

    @testfunc
    def age(self):
        return self._age
                
t = test()   
print(t.age)  # 输出18
```

通过类装饰器testfunc 保存好age 函数,而且这个属性age也变成了testfunc类型,所以age是属性(非数据)描述符,所以当我们访问age这个属性的时候,就会调用get方法,而且还会传递实例对象和类对象过去,我们正好利用实例对象执行这个方法得到数据返回

这里我们只实现了get方法,那要是要设置set方法呢? 那就必须在test里面重载一个age方法,而且必须使用原先的age修饰器对象重新建一个新的对象,把set 和 get 方法都保存好

```python
class testfunc:
    def __init__(self,get = None,set = None) -> None:
        self.get = get
        self.set = set
    def __get__(self,instance,owner):
        return self.get(instance)
    
    def __set__(self,instance,value):
        return self.set(instance,value)
    
    def setter(self,set):
        print("in setter")
        return testfunc(self.get, set)
        
class test:
    def __init__(self) -> None:
        self._age = 18

    @testfunc
    def age(self):
        return self._age
    print(age) 
    @age.setter
    def age(self,_age):
        self._age = _age
    print(age)   
t = test()  
t.age = 28 
print(t.age)  # 输出28
```

在 test 类中 我们 打印了两次 age修饰器对象,发现两个是不一样的,但是最终又只有一个age对象存在类中,所以我们必须用原先的装饰器对象创建一个新的装饰器对象,这样才能把所有的 get set 方法 保存下来

### 所有实例共享数据描述符

先看看下面这种

```python
class Score:
    def __init__(self,score) -> None:
        self.score = score
    def __get__(self,instance,owner):
        return self.score
    def __set__(self,instance,value):
        if value < 0 or value > 100:
            raise Exception("value invalid")
        self.score = value

class Student:
    score = Score(0)
    
    def __init__(self,score):
       self.score = score

student = Student(60)
student2 = Student(100)
print(student.score)  # 100
print(student2.score) # 100
```

我们惊奇的发现student 与 student2的 值居然一样了,这种数据描述符是有问题的,我们需要修改get 和 set方法,让他们返回和各个实例的属性值(但是这不意味着当我们通过实例访问与类同名的实例属性的时候就是直接访问它,其实还是访问的 类的dict,只不过我们根据不同实例返回不同值罢了

```python
class Score:
    def __init__(self,name) -> None:
        self.name = name
    def __get__(self,instance,owner):
        return instance.__dict__[self.name]
    def __set__(self,instance,value):
        if value < 0 or value > 100:
            raise Exception("value invalid")
        instance.__dict__[self.name] = value

class Student:
    math = Score("math")
    chinese = Score("chinese")
    
    def __init__(self,math,chinese):
       self.math = math
       self.chinese = chinese

student = Student(60,60)
student2 = Student(100,100)
print(student.math,student.chinese) # 60 60
print(student2.math,student2.chinese) # 100 100
```

这样就可以啦,当我们进入Score 的 get 和 set 方法的时候,我们返回他们自己对应的属性,记得一定要用 dict 不要直接 .  因为使用 dict 不会触发 get 和 set 方法

### getattribute 和 getattr的区别

getattribute 对任何属性的获取都会走这个方法, 只不过如果我们使用object的getattribute来获得属性值的时候,如果不存在的话会走getattr

### 线程池的实现
