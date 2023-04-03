import numpy as np
a = np.array([1,2,3,4,5])
a[1] = 10
b = np.array([4,5,6,7,8])

print(type(a)) #<class 'numpy.ndarray'>
print(a+10) #[11 20 13 14 15]
# 注意和列表的区别
print(a*2) # [ 2 20  6  8 10]

a = [[1,2,3],[4,5,6]]
a = np.array(a)
print(a[1,1]) # 这里也是numpy独有的  5


