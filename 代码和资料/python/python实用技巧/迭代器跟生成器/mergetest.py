import heapq
a = [1,4,6,8,9]
b = [2,3,8,10,11]

print(list(heapq.merge(a,b))) # [1, 2, 3, 4, 6, 8, 8, 9, 10, 11]