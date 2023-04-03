import re
import os
import shutil
import sys

if len(sys.argv) < 2:
    print("没有给出文件路径")
    sys.exit(0)

srcname = sys.argv[1]
lname = sys.argv[2] if len(sys.argv) > 2 else "python"
ff = os.path.dirname(srcname)
destname = ff + r"\test.md"
print("待修改文件路径为:"+srcname)
print("临时存放文件路径为:"+destname)


with open(srcname,"r",encoding="utf-8") as file:
    filestr = ''
    
    for i in file:
        filestr += i
    
    codes = re.split("^```.*?$",filestr,flags=re.MULTILINE)
    i = 0
    file.close()
    with open(destname,"w",encoding="utf-8") as file2:
         while i+1 < len(codes):
             file2.write(codes[i])
             i+=1
             file2.write(f"```{lname}" +codes[i]+"```")
             i+=1
    flag = input("请核对临时文件,是否覆盖临时文件到待修改文件(y/n)")
    if flag.lower().startswith("y"):
        shutil.copy(destname,srcname)
        os.remove(destname)
        print("覆盖完成")
    else:
        print("取消覆盖")



        
