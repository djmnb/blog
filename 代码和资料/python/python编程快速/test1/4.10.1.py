def func(spam):
    lenth = len(spam)
    strs = ''
    
    for i in range(lenth-1):
        strs += spam[i] + ','
    if lenth >= 1:
        strs += 'and ' + spam[-1]
    return strs
spam = ['apples', 'bananas', 'tofu', 'cats']
print(func(spam))
