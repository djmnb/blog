from functools import partial

def func(a,b,c,d):
    return a+b+c+d

three = partial(func,1)
two = partial(func,1,d=4)
one = partial(func,1,2,3)
print(three(2,3,4))
print(two(2,3))
print(one(4))
