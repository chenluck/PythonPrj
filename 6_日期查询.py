year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))

import datetime

date1 = datetime.date(year, month, day)
date2 = datetime.date(year-1, 12, 31)
timedelta= (date1 - date2).days

print(date1)
print(date2)
print(f"这是这一年的第{timedelta}天")
