from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args,**kwds):
        print(f"{func}被调用")
        return func(*args,**kwds)
    return wrapper

@logger
def func(a,b):
   a-=1
   b-=1
   return a+b

print(func.__name__)  # 如果不使用wraps会输出wrapper,使用wraps会输出func

