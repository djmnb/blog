class Node:
    def __init__(self,value) -> None:
        self._value = value
        self.left = None
        self.right = None
    def setleft(self,node):
        self.left = node
    def setright(self,node):
        self.right = node
    def __iter__(self):
        return helpIterator(self)
    def __str__(self) -> str:
        return f"node({self._value})"

class helpIterator:
    def __init__(self,node) -> None:
        self.node = node
        self.leftiter = None
        self.rightiter = None
    def __iter__(self):
        return self
    def __next__(self):
        if self.node == None:
            raise StopIteration
        if self.leftiter is None:
            self.leftiter = iter(helpIterator(self.node.left))
            return self.node
        elif self.rightiter is None:
            try:
                value = next(self.leftiter)
                return value
            except StopIteration as s:
                self.rightiter = iter(helpIterator(self.node.right))
                return next(self)
        else:
            return next(self.rightiter)
    

root = Node(10)
left = Node(11)
right = Node(14)
root.setleft(left)
root.setright(right)
left.setleft(Node(12))
left.setright(Node(13))
right.setleft(Node(15))
right.setright(Node(16))

for val in root:
    print(val)

