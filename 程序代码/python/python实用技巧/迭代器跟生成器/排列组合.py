import itertools
l = [1,2,2]


# 选取前N个数据进行排列
for i in itertools.permutations(l,3): 
    print(i)  # 返回的是一个元组

# 选取N个数据进行组合,N个数据不能选取同一个位置
for i in itertools.combinations(l,2):
    print(i)

# 选取N个数据进行组合,N个数据能选取同一个位置
for i in itertools.combinations_with_replacement(l,2):
    print(i)