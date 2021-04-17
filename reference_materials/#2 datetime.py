"""
strftime reference: https://strftime.org/

"""
#%%
import datetime
#DATETIME MODULE
now = datetime.datetime.now()
print(now.strftime('%d %B %Y - %X'))
print(f'testing datetime object in fstring {now: %d %B %Y - %X}')

#%%
#DATETIME METHOD
print(now.year)
print(now.month)
print(now.day)

#%%
#TIMEDELTA MODULE
add_time = datetime.timedelta(days=2, hours=3, minutes=15) # to create a time delta object
future = now + add_time
print(future)
#%%
#DATE MODULE
today = datetime.date.today()
some_date = datetime.date(year=2020, month=12, day=25) # to create a date object
print(some_date)
print(type(some_date))

some_date + add_time