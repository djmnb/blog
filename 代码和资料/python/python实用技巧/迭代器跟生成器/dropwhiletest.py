import itertools

def testiter():
   a = [i for i in range(20)]
   yield from a

it = testiter()

# 当数据小于5的时候就丢弃
print(list(itertools.dropwhile(lambda x:x<5,it))) # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]