from itertools import groupby
from operator import itemgetter
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
# 必须先排好序
rows.sort(key=itemgetter("date"))

# 根据日期分组,得到每个分组里面数据,以及分组数量
groups = 0
for date, items in groupby(rows,key=itemgetter("date")):
    groups += 1
    print(f'第{groups}分组的内容为:')
    for item in items:
        print(item)
