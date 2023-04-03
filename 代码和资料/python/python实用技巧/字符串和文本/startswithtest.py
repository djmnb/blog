url = "http://www.baidu.com"

def ishttp(url):
    return url.startswith(("http","https"))
print(ishttp(url))