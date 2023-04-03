import fnmatch

print(fnmatch.fnmatch("A.TXT","*.txt")) # windows下为True  linux下为False
print(fnmatch.fnmatchcase("A.TXT","*.txt")) # False
