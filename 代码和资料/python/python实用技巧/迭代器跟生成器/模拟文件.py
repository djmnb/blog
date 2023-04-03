import io

files = io.StringIO("helloworld")
print(files.read())

fileb = io.BytesIO(b'hello world')
print(fileb.read())