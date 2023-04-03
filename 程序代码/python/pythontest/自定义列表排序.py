import random
import pprint

nums = [ [int(random.random()*100) for i in range(10)] for j in range(10)]
pprint.pprint(nums)
print("------------------")
nums.sort(key=lambda x:x[0])
pprint.pprint(nums)