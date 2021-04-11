#%%
import calendar
import datetime

now = datetime.datetime.now()

print(calendar.month(2021,1))
print(calendar.month(now.year, now.month))
