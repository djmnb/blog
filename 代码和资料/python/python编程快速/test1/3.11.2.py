import testm as s
while True:
    try:
        num = int(input("输入一个数"))
        break
    except Exception:
        print("请输入整数")

while num != 1:
    num = s.collatz(num)
