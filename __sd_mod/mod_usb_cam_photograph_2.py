import os
import sys
sys.    path.append("/home/pi/_py/__sd_mod")
import mod_time_get

def Take_a_photo(n):
    filename_val = str(mod_time_get.dt_now_year()) + str(mod_time_get.dt_now_month()) + str(mod_time_get.dt_now_day()) + '-' + str(mod_time_get.dt_now_hour()) + str(mod_time_get.dt_now_minute()) + str(mod_time_get.dt_now_second())
    try:
        if int(n) == 0:
            print("err:Enter a number greater than 0 in the command argument.")  
        else:
            for i in range(int(n)):
                os.system("fswebcam -r 1920x1080 " + filename_val + "-" + str(i + 1) + '.jpg')
    except:
        print("err:Enter a number for the command line argument.")
