import datetime
import pytz
'''
tday = datetime.date.today()
bday = datetime.date(2024, 6, 5)

till_bday = bday - tday

print(till_bday.days)
'''

#print(tday)

tdelta = datetime.timedelta(days = 7)

#print(tday + tdelta)

t = datetime.time(9, 30, 45, 100000)
t2 = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

print(t)
print(t.hour)
print(t2)
print(t2 + tdelta)
print(' ')
for tz in pytz.all_timezones:
    print(tz)



