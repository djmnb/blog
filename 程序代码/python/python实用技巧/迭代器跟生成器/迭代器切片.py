import itertools

def testiter():
   a = [i for i in range(20)]
   yield from a

it = testiter()

print(list())


print(list(itertools.islice(it,5))) 