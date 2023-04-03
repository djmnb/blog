import time
a = "10"
b = "20"

n = 1000000

start = time.time()
s = ""
for i in range(n):
    s += a+b
end = time.time()
print(f"+拼接字符串耗时{end-start}s") #1.0576465129852295s
start = time.time()
s = ""
s = s.join(a+b for i in range(n))
end = time.time()
print(f"join拼接字符串耗时{end-start}s") # 0.15259289741516113s


