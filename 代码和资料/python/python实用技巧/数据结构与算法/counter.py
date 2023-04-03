from collections import Counter
import random

a = [int(random.random()*3) for i in range(5)]
b = [int(random.random()*3) for i in range(5)]
print(a)  # [2, 2, 0, 0, 2]
print(b) # [2, 2, 1, 1, 0]

# Counter跟dict的方法差不多
ca = Counter(a)
cb = Counter(b) 
print(ca)  # Counter({2: 3, 0: 2})
print(cb)  # Counter({2: 2, 1: 2, 0: 1})

# 求出前2个数量最多的,列表里面套元组,而且是已经排好序的
print(ca.most_common(2))  # [(2, 3), (0, 2)]
print(cb.most_common(2))  #  [(2, 2), (1, 2)]

# 做数学运算
print(ca-cb) # Counter({2: 1, 0: 1})
print(ca+cb) # Counter({2: 5, 0: 3, 1: 2})

class A:
    def __init__(self) -> None:
        self.a = 10
    def __getitem__(self,key):
        return self.__dict__[key]
a = A()
print(a["a"])