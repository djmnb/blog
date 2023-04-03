import os

filepath = r"C:\Users\asus\Desktop\hexoblog\source\_posts\python\代码文件\python实用技巧\迭代器跟生成器\ostest.py"

print(os.path.basename(filepath)) # 文件名字 ostest.py
print(os.path.dirname(filepath))  # 目录名字
print(os.path.isabs(filepath))    # 是否是绝对路径  True
print(os.path.isdir(filepath))    # 是否是目录 False
print(os.path.isfile(filepath))   # 是否是文件 True
print(os.path.islink(filepath))   # 是否是链接文件 False
print(os.path.ismount(filepath))  # 是否是挂载文件 False
print(os.path.exists(filepath))   # 文件是否存在  True
print(os.path.getsize(filepath))  # 文件大小



import time
def strftime(seconds):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(seconds))
print(strftime(os.path.getatime(filepath)))  # 上一次文件访问时间
print(strftime(os.path.getmtime(filepath)))  # 上一次文件修改时间
print(strftime(os.path.getctime(filepath)))  # 上一次文件元信息修改时间 比如文件名字更改 文件权限变化


os.




