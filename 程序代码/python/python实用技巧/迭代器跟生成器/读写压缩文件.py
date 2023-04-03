import gzip


with gzip.open("test.gz","wb") as f:
    f.write(b"12345")

