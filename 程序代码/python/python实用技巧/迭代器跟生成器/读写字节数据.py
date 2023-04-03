txt = "hello world"

with open("test.bin","wb") as f:
    data = txt.encode("utf-8")
    n = 100
    [f.write(data) for i in range(n)]
    print(n*len(data))

from functools import reduce

with open("test.bin","rb") as f:
    print(reduce(lambda a,b:a+len(b),iter(f.read,b''),0))
