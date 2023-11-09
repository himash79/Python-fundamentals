# Date and Time :
# Below examples provides date and time functions.

import datetime as dt

print('Initiate date ==========================')
dateTime = dt.date(2002,4,12)
print(dateTime)

print('Initiate current date ==========================')
dateTimeCurrent = dt.date.today()
print(dateTimeCurrent)
print(dateTimeCurrent.month)
print(dateTimeCurrent.day)


print('Initiate format time and dates ==========================')
dateTimeFormatted = dateTime.strftime('%A, %B, %d, %Y')
print(dateTimeFormatted)

print('Initiate week day ==========================')
week = dateTime.weekday()
print(week)

print('Initiate ISO week day ==========================')
isoWeek = dateTime.isoweekday()
print(isoWeek)

print('Initiate time ==========================')
time = dt.time(9,30,59,10000)
print(time)

print('Initiate before date and after ==========================')
beforeDate = dt.timedelta(days = 10)
print(dateTimeCurrent - beforeDate)