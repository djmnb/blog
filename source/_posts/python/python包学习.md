---
title: python常用包学习
date: 2025-3-9
---

# Numpy

## 提取数据

### 1. 索引

这种方式就跟数组的使用是一模一样的

```python
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr[0] # [1,2,3]
arr[0,0] # [1]  等价于arr[(0,0)]
arr[[0,1]] # [[1,2,3],[4,5,6]]
```

### 2.切片

其实索引就是一种特殊切片, 我个人觉得可以这么理解

```python
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr[0] # [1,2,3] 等价于 arr[0,:]
arr[[0,1]] # [[1,2,3],[4,5,6]] 等价于arr[[0,1], :]
```

### 总结

np里面的数组有多少维度, 默认取数据的时候, 就能指定多少维度, 不指定就是全选, 默认维度指定是从左到右

通过这种理解方式, 我们就很容易得知取了数据之后还有多少维度

**需要注意的点就是 () 和 [] 的区别, () 就相当于正常取数据里面有个数据就是设置几个维度, 而[]只是设置一个维度** 

```python
a[(1,2,3)] => a[1,2,3]
a[[1,2,3]] => a[[1,2,3], :]
```

