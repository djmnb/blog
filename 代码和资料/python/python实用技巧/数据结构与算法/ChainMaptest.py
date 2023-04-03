from collections import ChainMap
a = {'x':1,'y':2}
b = {'x':2,'z':3}

m = ChainMap(a,b)
print(m["x"])  # 1
print(m["z"])  # 3
m["u"] = 10  #  相当于 a["u"] = 10
print(m) # ChainMap({'x': 1, 'y': 2, 'u': 10}, {'x': 2, 'z': 3})
