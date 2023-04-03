import random
num = random.randint(0,100)
inputnum = input("猜一个数字吧")
while True:
     inputnum = int(inputnum)
     if inputnum == num:
          break
     if inputnum < num:
          print("数字太小了哦",end='')
     else:
          print("数字太大了哦",end="")
     inputnum = input("再猜一个数字吧")
print('恭喜回答正确')
