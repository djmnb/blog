def func(n):
    def add():
        nonlocal n
        n = n+1
    return add
b = func(10)
b()