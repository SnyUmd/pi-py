
# -*- coding: utf-8 -*-
# coding: utf-8
import sys
import time
import datetime

import http.server
import socketserver


import webbrowser

#sys.path.append("/home/pi/_py/__sd_mod")
#import mod_webserver as mod_wb
sys.path.append("/home/pi/_py/__sd_mod/mod_gCalendar")
import mod_gCalendarCtrl as mod_GC



#**********************************************************
'''
def mWebServerRun():
    try:
        PORT = 8000
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()
        return True
    except:
        return False
'''
#**********************************************************
#def mWebServerRun2():

                
#**********************************************************
def mFileWrite_text(str_filename, str_html_text):
    strNL = '\n'
    str_html_val = '<html>' + strNL + \
                    '<body>' + strNL + \
                    str_html_text + strNL + \
                    '</body>' + strNL + \
                    '</html>'
    str_html_val.encode('shift_jis')
    #print(str_html_val)
    f = open(str_filename, 'w')
    f.write(str_html_val)
    f.close()


cntTest = 0

#**********************************************************
if __name__ == '__main__':
    while True:
        try:
            room1_val = ''
            room2_val = ''
            room3_val = ''
            str_html_txt = ''
            iNum = 3
            str_file_name = '/home/pi/_py/google_calendar/index.html'
            dt_now = datetime.datetime.now()
        
            cl_id = 'skydisc.jp_3130303935323631313837@resource.calendar.google.com'
            events = mod_GC.set_Calendar_API(cl_id, iNum)
            room1_val = mod_GC.read_calendar_now(events, False)
            #print(room1_val)
            #mDataTypeChange_Ary(room1_val)
        
            cl_id = 'skydisc.jp_34313237303839303238@resource.calendar.google.com'
            events = mod_GC.set_Calendar_API(cl_id, iNum)
            room2_val = mod_GC.read_calendar_now(events, False)
            #print(room2_val)
            
            cl_id = 'skydisc.jp_3638353434303437393537@resource.calendar.google.com'
            events = mod_GC.set_Calendar_API(cl_id, iNum)
            room3_val = mod_GC.read_calendar_now(events, False)
            #print(room3_val)
            
            str_html_txt = str(cntTest) + '\n'
            str_html_txt += str(dt_now) + '\n'
            str_html_txt += room1_val + '\n**********\n' + room2_val + '\n**********\n' + room3_val
            str_html_txt = str_html_txt.replace('\n', '<br />')
        
            mFileWrite_text(str_file_name, str_html_txt)
            print(cntTest)
            time.sleep(5)
            cntTest += 1
        except:
            print('error retry')
            time.sleep(5)
    
    '''
    #----------------
    flgLoop = True
    iCntLoop = 1
    iStopNum = 5
    while flgLoop:
        if mWebServerRun():
            flgLoop = False
        else:
            if iCntLoop == 1:
                print('retry')
                print('.')
            else:
                if iCntLoop > iStopNum:
                    print('err stop')
                    flgLoop = False
                else:
                    print('.')
            time.sleep(15)
            iCntLoop += 1
    #----------------
    '''