
l = [1,2,3,4,5]
a,b,c,d,e = l

# 如果数量不匹配则会报错
# a,b = l   # ValueError: too many values to unpack (expected 2)

# 如果我们只想要一些数据的话,可以用占位符(可以是任何字符,我们习惯用_),_代表占用一个 *_ 代表占用一群

_ , a , *_ = l
print(a) # 2


def average(socres):
    first,*mid,last = socres
    return sum(mid) / len(mid)

socres = [1,2,3,4,5]
last,*args = socres
print(average(args))




