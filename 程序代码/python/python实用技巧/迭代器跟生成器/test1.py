a = {1,2,3,4,5}
b = {1,2,3,4,5}

# 循环求和
sums = 0
for i in a:
    sums += i
for i in b:
    sums += i

print(sums)



# 使用chain
import itertools
print(sum(itertools.chain(a,b)))


def func():
    yield 10

from collections import Iterable

a = func()
