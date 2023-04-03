num = int(input("输入一个数"))
def collatz(num):
    if num % 2 == 0:
        print(num//2)
        return num //2
    else:
        print(num*3+1)
        return num*3+1
while num != 1:
    num = collatz(num)
