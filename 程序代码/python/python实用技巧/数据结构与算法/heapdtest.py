import heapq
nums = [10,34,1,3,5]
heapq.heapify(nums)  # 必须得先进行排序
print(heapq.heappop(nums)) # 删除堆顶
heapq.heappush(nums,20) # 添加一个元素
print(nums)
