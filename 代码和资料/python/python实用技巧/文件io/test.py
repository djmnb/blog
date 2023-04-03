with open(r"C:\Users\asus\Desktop\hexoblog\source\_posts\python\代码文件\python实用技巧\文件io\test.py",encoding="utf-8") as f:
    print(''.join(iter(f.read,'')))