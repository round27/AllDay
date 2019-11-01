#Example 1: Get Current Date and Time
import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)


#Example 2: Get Current Date
import datetime

date_object = datetime.date.today()
print(date_object)

print(dir(datetime))

#Example 3: Date object to represent a date
import datetime
d = datetime.date(2019, 4, 13)
print(d)

from datetime import date
a = date(2019, 4, 13)
print(a)

from datetime import date

a = date(2019, 4, 13)
print(a)

#Example 4: Get current date
from datetime import date
today = date.today()
print("Current date =", today)

#Example 5: Get date from a timestamp
#The number of seconds between a particular date and January 1, 1970 at UTC. 

from datetime import date
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

#Example 6: Print today's year, month and day
from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#A time object instantiated from the time class represents the local time.
#Example 7: Time object to represent time

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

#Example 8: Print hour, minute, second and microsecond
from datetime import time
a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

#Example 9: Python datetime object
from datetime import datetime

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

#Example 10: Print year, month, hour, minute and timestamp
from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

"""
datetime.timedelta
A timedelta object represents the difference between two dates or times.
Example 11: Difference between two dates and times
"""

from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))  

#Example 12: Difference between two timedelta objects
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("t3 =", t3)

#Example 13: Printing negative timedelta object
from datetime import timedelta

t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))

#Example 14: Time duration in seconds
#You can get the total number of seconds in a timedelta object using total_seconds() method.
from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())

"""
Python has strftime() and strptime() methods to handle this.
Python strftime() - datetime object to string
The strftime() method is defined under classes date, datetime and time. The method creates a formatted string from a given date, datetime or time object.
"""

#Example 15: Format date using strftime()
from datetime import datetime

# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

"""
	%Y - year [0001,..., 2018, 2019,..., 9999]
	%m - month [01, 02, ..., 11, 12]
	%d - day [01, 02, ..., 30, 31]
	%H - hour [00, 01, ..., 22, 23
	%M - min [00, 01, ..., 58, 59]
	%S - second [00, 01, ..., 58, 59]
"""

#Example 16: strptime()
from datetime import datetime
date_string = "21 June, 2018"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
