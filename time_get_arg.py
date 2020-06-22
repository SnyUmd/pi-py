import datetime
import sys

args = sys.argv

dt_now = datetime.datetime.now()

if args[1] == 'year' :
    print(dt_now.year)
elif args[1] == 'month':
    print(dt_now.month)
elif args[1] == 'day':
    print(dt_now.day)
elif args[1] == 'hour':
    print(dt_now.hour)
elif args[1] == 'minute':
    print(dt_now.minute)
elif args[1] == 'second':
    print(dt_now.second)
elif args[1] == 'microsecond':
    print(dt_now.microsecond)
else:
    print('err')