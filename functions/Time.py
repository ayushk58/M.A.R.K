import time
from datetime import datetime
import functions.Response
import assistant


class Time:
    def __init__(self):
        pass
    def check_time(self):
        current=datetime.now()
        hour=current.hour
        minute=current.minute
        if(hour>12 and hour<24):
            hour=hour-12
            functions.Response.say("The time is"+str(hour)+"PM"+str(minute)+"minutes" )
        else:
            functions.Response.say("The time is"+str(hour)+"AM"+str(minute)+"minutes" )
        

class Date:
    def __init__(self):
        pass
    def check_date(self):
        current=datetime.now()
        day=current.date
        year=current.year
        month=current.month
        functions.Response.say("Today is"+str(day)+"of"+str(month)+"of the year"+str(year))
    def check_month(self):
        current=datetime.now()
        month=current.month
        functions.Response.say("It is the month of"+str(month))
    def check_year(self):
        current=datetime.now()
        year=current.year
        functions.Response.say("It is the year of"+str(year))

def check(data):
    t1=Time()
    t2=Date()
    if "time" in data:
        t1.check_time()
    elif "date" in data:
        t2.check_date()
    elif "month" in data:
        t2.check_month()
    elif "year" in data:
        t2.check_year()

    