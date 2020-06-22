from subprocess import check_output
import os

year_val = check_output(["python", "time_get_arg.py", "year"]).decode('utf-8') 
year_val = year_val[0:len(year_val) - 1] 

month_val = check_output(["python", "time_get_arg.py", "month"]).decode('utf-8')
month_val = month_val[0:len(month_val) - 1]
if len(month_val) < 2:
    month_val = '0' + month_val
    
day_val = check_output(["python", "time_get_arg.py", "day"]).decode('utf-8')
day_val = day_val[0:len(day_val) - 1]
if len(day_val) < 2:
    day_val = '0' + day_val
    
hour_val = check_output(["python", "time_get_arg.py", "hour"]).decode('utf-8')
hour_val = hour_val[0:len(hour_val) - 1]
if len(hour_val) < 2:
    hour_val = '0' + hour_val
    
minute_val = check_output(["python", "time_get_arg.py", "minute"]).decode('utf-8')
minute_val = minute_val[0:len(minute_val) - 1]
if len(minute_val) < 2:
    minute_val = '0' + minute_val
    
second_val = check_output(["python", "time_get_arg.py", "second"]).decode('utf-8')
second_val = second_val[0:len(second_val) - 1]
if len(second_val) < 2:
    second_val = '0' + second_val

filename_val = year_val + month_val + day_val + '-'+ hour_val + minute_val + second_val + '.jpg'
#print(filename_val)

os.system("fswebcam -r 1920x1080 " + filename_val)
