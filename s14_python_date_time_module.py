import datetime

mytime = datetime.time(2, 20, 1, 20)

print(mytime)
print(mytime.hour)
print(mytime.minute)
print(mytime.second)
print(mytime.microsecond)

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

print(today.ctime())

mydatetime = datetime.datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime)
mydatetime = mydatetime.replace(year=1999)
print(mydatetime)

date1 = datetime.date(2021, 11, 3)
date2 = datetime.date(2020, 11, 3)

date_diff = date1 - date2
print(date_diff)

datetime1 = datetime.datetime(2021, 11, 3, 22, 0)
datetime2 = datetime.datetime(2020, 11, 3, 12, 0)
datetime_diff = datetime1 - datetime2
print(datetime_diff)
