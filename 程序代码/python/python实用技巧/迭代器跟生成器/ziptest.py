for i,j in zip(range(10),range(11,0,-1)):
    print((i,j))

# (0, 11)
# (1, 10)
# (2, 9)
# (3, 8)
# (4, 7)
# (5, 6)
# (6, 5)
# (7, 4)
# (8, 3)
# (9, 2)

# 如果需要最长的为主的话
import itertools
for i,j in itertools.zip_longest(range(10),range(11,0,-1)):
	print((i,j))
        
# (0, 11)
# (1, 10)
# (2, 9)
# (3, 8)
# (4, 7)
# (5, 6)
# (6, 5)
# (7, 4)
# (8, 3)
# (9, 2)
# (None, 1)