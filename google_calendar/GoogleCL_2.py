# coding: utf-8
import sys

import http.server
import socketserver
#sys.path.append("/home/pi/_py/__sd_mod")
#import mod_webserver as mod_wb
#sys.path.append("/home/pi/_py/__sd_mod/mod_gCalendar")
import mod_gCalendarCtrl as mod_GC



#**********************************************************
def mWebServerRun():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
                
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


#**********************************************************
if __name__ == '__main__':
    iNum = 3
    #str_file_name = '\C:\Users\shume\Documents\_umd\github_umd\pi-py\google_calendar/index.html'
    str_file_name = 'index.html'
    
    cl_id = 'primary'
    events = mod_GC.set_Calendar_API(cl_id, iNum)
    event_val = mod_GC.read_calendar_now(events, False)
    print(event_val)
    #mDataTypeChange_Ary(room1_val)

    
    mWebServerRun()