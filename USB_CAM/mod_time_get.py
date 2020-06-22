import datetime
import sys

args = sys.argv

def dt_now_year():
    dt = datetime.datetime.now()
    return dt.year
    
def dt_now_month():
    dt = datetime.datetime.now()
    return dt.month
    
def dt_now_day():
    dt = datetime.datetime.now()
    return dt.day
    
def dt_now_hour():
    dt = datetime.datetime.now()
    return dt.hour
    
def dt_now_minute():
    dt = datetime.datetime.now()
    return dt.minute
    
def dt_now_second():
    dt = datetime.datetime.now()
    return dt.second
    
def dt_now_microsecond():
    dt = datetime.datetime.now()
    return dt.microsecond
"""
print(str(dt_now_year()) + ' ' + str(dt_now_month()) + ' ' + 
        str(dt_now_day())  + ' ' + str(dt_now_hour()) + ' ' + 
        str(dt_now_minute())  + ' ' + str(dt_now_second())  + ' ' + str(dt_now_microsecond()))
"""
