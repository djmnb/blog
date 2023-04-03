import re

text = 'yeah, but no, but yeah, but no, but yeah'

# replace 默认全部替换,我们也可以限制替换数量
print(text.replace("yeah","yep")) # yep, but no, but yep, but no, but yep
print(text.replace("yeah","yep",2)) # yep, but no, but yep, but no, but yeah

text = 'now is 3/17/2023, now is 3/17/2023'
# sub 中的 替换字符串正则表达式可以使用 匹配字符串中的分组
print(re.sub(r"(\d{1,2})/(\d{1,2})/(\d{4})",r'\3-\2-\1',text)) # now is 2023-17-3, now is 2023-17-3

# 还可以指定替换数量
print(re.sub(r"(\d{1,2})/(\d{1,2})/(\d{4})",r'\3-\2-\1',text,1)) # now is 2023-17-3, now is 3/17/2023

# 如果替换逻辑比较复杂,我们也可以用回调函数,函数的参数类型为 re.Match
def func(m): 
    print(m)
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
print(re.sub(r"(\d{1,2})/(\d{1,2})/(\d{4})",func,text)) # now is 2023-17-3, now is 2023-17-3

# 我们还可以用subn获得替换了多少次
print(re.subn(r"(\d{1,2})/(\d{1,2})/(\d{4})",r'\3-\2-\1',text)) # ('now is 2023-17-3, now is 2023-17-3', 2)

