import random
a = [1,2,3,4,5]

# 随机选一个
print(random.choice(a))
# 随机选多个,可以包含位置的数
print(random.choices(a,k=3))
# 随机选出多个不同位置的数,注意是位置,如果列表中的数不同,选出来的数肯定也不相同
print(random.sample(a,3))
# 打乱顺序
random.shuffle(a)
print(a)
# 随机产生一个[a,b]之间的整数
print(random.randint(10,20))
# 随机产生一个[0,1)的小数
print(random.random())