---
title: Python编程快速上手 总结
date: 2023-3-4
tags:
  - python
  - 需要复习
---

> 编程是一项创造性任务

# 前言

> 程序开发要学会 **站在巨人的肩膀上** 。动手写代码前，先调研一番，看是否有现成的解决方案。 **切忌重复造轮子** ，浪费时间不说，可能代码质量还差，效果也不好。

这个是基于python 3.8 总结的

在 *Python* 中，一切皆对象，基本数据类型也是如此

[参考文档](https://python.iswbm.com/index.html#)

# 第一部分 python 基础

## 相对路径

包导入相对路径规则: 相对于import语句所在的py文件本身位置(并且有相对导入的文件不能直接执行, 得通过python -m)

包导入绝对路径规则(就是没有相对路径, 而不是文件那样的绝对路径): 将当前执行的py文件所在路径加载到sys.path, 然后还有一些内置的路径一起放到sys.path



文件相对路径规则:  相对于当前python执行所在的目录位置, 与执行的py文件路径无关



# 第二部分 自动化

## 正则表达式

> 关于什么是正则表达式,我已经在我的另外一篇博客里面介绍清楚了,这里只做关于python如何使用正则表达式的总结

python的正则表达式的使用有两种:

第一种就是 直接使用 re 模块里面的函数 比如 re.search(pattern,string,flags) re.match() re.findall() ... 

第二种就是 使用re.compile(pattern,flags)  得到一个对象,然后调用这个对象的search(string),match findall 方法

第一种呢,方便我们一次性使用,第二种方便一个匹配模式多次使用

### search方法

搜索第一个匹配的字符串,并且返回包含这个字符串的匹配对象

### match方法

从开头开始匹配,如果没有匹配成功,则不会继续匹配

### findall方法

**返回全部匹配的字符串的所有分组(0分组除外,如果只有0分组的话就必须包含0分组)**,并且都放在列表中返回

### finditer方法

匹配所有字符串,而且**我们可以迭代遍历所有的匹配对象**

四个方法总结一下吧:

如果我们只是想看某个字符串是否包含这个模式,我们可以使用search

如果我们要看从开头是否匹配,使用match

如果只需要得到所有匹配结果的分组,使用findall

如果要获得所有的匹配字符串,还要获得所有的匹配字符串的分组,使用finditer

## 读写文件

# 好用的功能

## **格式化字符串**

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

   

## 不一样的作用域

在python中,貌似对这个代码块作用域不太敏感

```python
if 1 == 1:
    a = 10
print(a)  # 输出10
```

如果在c++和 java中,这个代码肯定会报错,我去,那这样也太爽了

## \_\_call\_\_方法

a.\_\_call\_\_ () == a()  这么一来,我感觉函数跟类其实也没有什么区别

## type返回值

type的返回值就是一个类,他也是一个对象,因此我们是不是可以根据某个数据直接造出跟它一样类型的对象

```python
def getobj(obj):
    return type(obj)()
print(getobj(111))
print(getobj("111"))
print(getobj([]))
print(getobj({}))
```

## 切片

对于列表,元组,字符串这种,我们都可以使用切片来获得他们的子序列,  而且切片是可以越界的, 只会返回包含的数据

```
a = [1,2,3]
print(a[1:10:1]) # [2,3]
```



# 额外补充

## 可变对象与不可变对象

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

## 对象属性访问和创建的规则

* 当我们对一个实例属性进行访问时，Python 会按 `obj.__dict__` → `type(obj).__dict__` → `type(obj)的父类.__dict__` 顺序进行查找

* 当我们对一个实例属性,**跟类属性不重名,或者类属性不是一个数据描述符**,进行赋值的时候,如果obj.\_\_dict\_\_ 里面不存在,那么就创建,如果存在则修改
* 当我们对一个实例属性,**跟类属性重名,而且类属性是一个数据描述符**,进行赋值的时候, 一定是按照这个顺序`type(obj).__dict__` → `type(obj)的父类.__dict__` 去修改数据

## property实现原理

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

## 所有实例共享数据描述符

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

## 类装饰器注意点

在使用**类装饰器**修饰**类方法**时候,我们还必须得实现\_\_get\_\_ 这个方法,这是因为类方法属于一个属性,当我们通过类或者对象通过点去调用它的时候,会走\_\_get\_\_ 这个函数得到返回值再执行,所以我们的通过对象调用方法不需要再传递self,是因为function的\_\_get\_\_帮我们传递了,因此我们也需要自己在类修饰器的\_\_get\_\_里面传递self,  而**函数装饰器我们就不需要去管这件事**

## 多个装饰器需要注意的点

多个装饰器最需要注意的点是 后一个装饰器返回的东西到底是什么,是一个函数还是一个对象还是一个属性描述符,函数和可调用对象调用起来需要几个参数, 如果是一个属性描述符而且我们需要他的get方法被调用的话则必须位于第一个装饰器,所以像@staticmethod 和 @ classmethod 这些就必须放在最前面

## getattribute 和 getattr的区别

**getattribute 对任何属性的获取都会走这个方法**,  如果我们没有重写这个方法,  默认会调用object.\_\_getattribute\_\_这个方法,如果找到了访问的属性就会返回,如果没有找到就会调用getattr方法, 如果都没有找到就会报错

## 线程池的实现



## 设置清华源

### 临时使用

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

### 设为默认

升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

```
python -m pip install --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

```
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
```

# 答疑解惑

## 为什么类没有实现call方法却可以被调用()生成对象

哈哈哈,这里确实是一个迷惑点,  其实类也是一个对象,它是元类的对象, 一个对象能不能像方法那样被调用,是要看创建它的类是否具有call方法, 所以我们在类中有没有声明的call方法跟类能不能创建对象没有任何关系,而跟它创建的对象能不能被调用才有关系,  真正跟类能不能调用是跟元类中有没有call方法有关系**,type 是所有类的父类**,而它具有call 方法,所以所有的类一定能被调用



## 实例对象属性的访问流程与赋值流程

### 默认访问流程(没有重写getattribute方法)

1. 调用object.`__getattribute__`方法。
2. 在类对象的`__dict__`中查找属性,如果是数据描述符,就调用它的get方法得到返回值返回,如果不是数据描述符就继续
3. 在实例对象的`__dict__`中查找属性。**如果找到了就返回这个值,没找到就继续往下走**
4. 在类对象的`__dict__`中查找属性。**处理方法、类变量和非数据描述符**
5. 调用`__getattr__`方法 (**这个方法一般需要我们重写,如果没有重写就不会调用,所以这个方法只有当属性找不到的时候才会被调用**)
6. 如果上述步骤都没有找到,抛出`AttributeError`异常。

### 默认赋值流程(没有重写setter方法)

1. 调用object.`__setattr__`方法。
2. 在类对象的`__dict__`中查找属性。如果找到一个属性而且是数据描述符(具有get和set方法,其实只有set方法也可以,但是只要set方法没有意义),就会调用这个属性set方法并且将值传递给他, 如果没有找到属性,或者这个属性不具有set方法,那么就会往下走
3. 将属性赋值到实例对象的`__dict__`。

**这里我们就能解释数据描述符了, 为什么我们在init方法的时候对一个数据描述符赋值不会赋值到自己的dict里面,而是调用了类属性的set方法**
