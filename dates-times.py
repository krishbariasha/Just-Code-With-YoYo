# Python Datetime

from datetime import datetime
from datetime import timedelta
from datetime import date
#current date and time
now = datetime.now()
print(f'The current date and time is : {now}')

#Display date and time in different formats

print(f'Current date: {now.date()}')

# Current Time
print(f'Current Time: {now.time()}')

#Format the date and time
print(f'Formated Datetime: {now.strftime("%Y-%m-%d %H:%M:%S")}')

#Get the dat of the Week

weekday = now.strftime('%A')
print(f'Weekday: {weekday}')


#Adding and subtrating date and time
delta = timedelta(days=1)
one_day_in_future = now + delta
print(f'One day in future: {one_day_in_future}')

#one day in Past
one_day_in_past = now - delta #delta means difference
print(f'One day in past: {one_day_in_past}')

#Specific Date
specific_date = date(2024,2,27)
print(f'The specific date is: {specific_date}')

