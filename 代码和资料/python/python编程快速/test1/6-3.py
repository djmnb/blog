import sys
import pyperclip
password = {'djm':'abc','qq':'hardwork'}
name = ''
if len(sys.argv) < 2:
    name = input('please input username\n')
else:
    name = sys.argv[1]

if name in password:
    pyperclip.copy(password[name])
    pyperclip.paste()
    print('password already is copied')
else:
    print('this is not recorded')
    
    
