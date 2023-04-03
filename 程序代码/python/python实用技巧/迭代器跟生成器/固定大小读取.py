
def gett(read,size):
    def reaffunc():
        return read(size)
    return reaffunc


with open("test.bin","rb") as f:
    for i in iter(gett(f.read,10),b''):
        print(len(i))


class test:
    def __init__(self,value) -> None:
        self.value = value
    def get(self):
        return self.value

t = test(100)
print(t)
print(test.get)
print(t.get)

def tt(t):
    print(t())

tt(t.get)
print(tt)
