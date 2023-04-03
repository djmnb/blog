import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

# 只能指定一个分隔符
print(line.split(';')) #['asdf fjdk', ' afed, fjek,asdf, foo']
print(line.split(',;')) # ['asdf fjdk; afed, fjek,asdf, foo']

# 可以指定多个分隔符
print(re.split(r'[ ,;]+',line)) #['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 如果指定分组的话分割好的列表中会包含分隔符
print(re.split(r'([ ,;]+)',line)) #['asdf', ' ', 'fjdk', '; ', 'afed', ', ', 'fjek', ',', 'asdf', ', ', 'foo']

print(re.split(" "," fdsfd"))


print(ord("1"))