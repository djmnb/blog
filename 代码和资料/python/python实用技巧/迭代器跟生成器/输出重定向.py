
a = [1,2,3]
with open("test.txt","wt",encoding="UTF-8") as f:
    print(*a,file=f,sep=",")