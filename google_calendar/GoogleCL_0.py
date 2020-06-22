# coding: utf-8
import sys
sys.path.append("/home/pi/_py/__sd_mod")
import mod_webserver as mod_wb
sys.path.append("/home/pi/_py/__sd_mod/mod_gCalendar")
import mod_gCalendarCtrl as mod_GC

#**********************************************************
if __name__ == '__main__':
    room1_val = ''
    room2_val = ''
    room3_val = ''
    iNum = 3
    
    cl_id = 'skydisc.jp_3130303935323631313837@resource.calendar.google.com'
    events = mod_GC.set_Calendar_API(cl_id, iNum)
    room1_val = mod_GC.read_calendar_now(events, False)
    print(room1_val)
    #mDataTypeChange_Ary(room1_val)
    
    cl_id = 'skydisc.jp_34313237303839303238@resource.calendar.google.com'
    events = mod_GC.set_Calendar_API(cl_id, iNum)
    room2_val = mod_GC.read_calendar_now(events, False)
    print(room2_val)
    
    cl_id = 'skydisc.jp_3638353434303437393537@resource.calendar.google.com'
    events = mod_GC.set_Calendar_API(cl_id, iNum)
    room3_val = mod_GC.read_calendar_now(events, False)
    print(room3_val)
    