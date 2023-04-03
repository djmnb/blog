a =-128

print(a.to_bytes(4,"big",signed=True)) # b'\xff\xff\xff\x80'

print(int.from_bytes(b'\xff\xff\xff\x80\x80',"big",signed=True))



# with open("test.bin","wb") as file:
#     file.write(a.to_bytes(4,"big",signed=True))