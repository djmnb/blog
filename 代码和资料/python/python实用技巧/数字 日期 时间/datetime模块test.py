import datetime

# timedelta代表的是一个时间段,可以设置天数,小时,分钟,秒,毫秒,微秒  小时会被转化成秒,微秒会转化成秒
fivedays = datetime.timedelta(days=5)
tendays = 2*fivedays  # 可以执行基本运算
print(tendays.days)  # 得到天数 10
print(tendays.seconds) # 0s
print(tendays.total_seconds())  # 得到全部秒数

#日期的运算
datea = datetime.datetime(2002,4,5)
dateb = datetime.datetime(2001,4,5)


# 运算结果是一个时间段,a-b 和 b-a结果一样
subdate = dateb-datea

print((datea-dateb).days) # 相差了 365天
print((datea-dateb).seconds) # 0s

# adddate = datea + dateb 日期与日期不支持加法

datec = datea + fivedays   #  日期与时间段支持加法
print(datec)   # 2002-4-10

datec = datetime.datetime(2023,3,17)

print(datec.year)
print(datec.month)
print(datec.day)
print(datec.weekday())  # 从0开始的 0代表星期一

# 计算上个周五的日期
now = datetime.datetime.now()
prefive = now-datetime.timedelta(7-(now.weekday()-4))
print(prefive.date())


import calendar




