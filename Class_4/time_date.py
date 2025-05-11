import time

# Getting the Current Time
current_time = time.localtime()
print(f"Current time : {current_time} \n")
print(f"Today is {current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday}.")


# Getting the Formatted Time
formatted_time = time.asctime(time.localtime())
print("Current time :", formatted_time)



# Getting the Calendar for a Month
import calendar

current_year = time.localtime().tm_year
current_month = time.localtime().tm_mon
print(calendar.month(current_year, current_month))


# The Date Time
from datetime import date

event_time = datetime.now()
print(f"Current time : {event_time}")

# Calculate birthday
today = date.today()
next_birthday = date(today.year, 7, 2) 
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_until = (next_birthday - today).days
print(f"Days until next birthday: {days_until}")


# The strftime() Method
import datetime

x = datetime.datetime(2025, 1, 1)
print(x.strftime("%f")) 
print(x.strftime("%A"))   
print(x.strftime("%Y")) 
print(x.strftime("%B"))   


# Math Module
import math

radius = 5
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Circle with radius {radius}:")
print(f"Circumference: {circumference:.2f}, Area: {area:.2f}")