from collections import deque

queue = deque(maxlen=5)
queue.extend([1,2,3,4,10,6,7])
for i in queue:
    print(i)




