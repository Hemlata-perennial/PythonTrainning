import time
print("seconds ",time.time())
print("current date and time:",time.ctime(time.time()))
print("local time: ",time.localtime())
print("date in user defined format: ",time.strftime("%d/%m/%y"))

import datetime
print(datetime.datetime.today())
print(datetime.datetime.now())
nowd=datetime.datetime.now()
print(nowd.month,nowd.day,nowd.year,nowd.hour)

import pytz
timezones=pytz.country_timezones("IN")
print(timezones)
pacific=pytz.timezone('Asia/Kolkata')
print(type(pacific),pacific)
localDt=pacific.localize(nowd)
print(localDt)