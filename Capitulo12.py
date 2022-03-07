"""
    Trabalhando com Data e Hora
"""
import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.year)

# Metodo strftime()
print(now.strftime("%A"))

# Módulo Calendario

import calendar
di = datetime.datetime.now()
print(di.year)
print(di.strftime("%A"))
cal_month = int(input("Enter the month (0-12): "))
cal_year = int(input("Enter the year (yyyy): "))
cal = calendar.month(cal_year, cal_month)
print(("You requested a calendar for", cal_year, cal_month))
print(cal)
year = int(input("Enter the year (yyyy): "))
cal = calendar.calendar(year)
print(cal)
print(calendar.weekday(2022, 3, 8))

# Time
import time

print(time.gmtime(0))

from time import time
print(time())

from time import ctime
print(ctime())

# Time Zones

import time
timet = (2019, 3, 10, 8, 50, 6, 6, 69, 1)
print(time.mktime(timet))

time.asctime(time.gmtime())
print(time.asctime(time.gmtime()))
print(time.asctime(time.localtime()))
