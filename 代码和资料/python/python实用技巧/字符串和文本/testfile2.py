import re
import os
import shutil
import sys


# 

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
    
    filestr = filestr.join(file)
    
    codes = re.sub(r"^```.*?$(.*?^```$)",rf"```{lname}\1",filestr,flags=re.MULTILINE|re.S)
    with  open(destname,"w",encoding="utf-8") as file2:
        file2.write(codes)
    file.close()
    flag = input("请核对临时文件,是否覆盖临时文件到待修改文件(y/n)")
    if flag.lower().startswith("y"):
        shutil.copy(destname,srcname)
        os.remove(destname)
        print("覆盖完成")
    else:
        print("取消覆盖")



        
