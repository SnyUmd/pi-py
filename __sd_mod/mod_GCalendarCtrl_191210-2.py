# coding: utf-8
'''
#memo
自分：primary
会議室1：'skydisc.jp_3130303935323631313837@resource.calendar.google.com'
会議室2：'skydisc.jp_34313237303839303238@resource.calendar.google.com'
会議室3：'skydisc.jp_3638353434303437393537@resource.calendar.google.com'
'''
#************1*************
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


#**********************************************************
#GoogleCalendarAPI　SET
#**********************************************************
def set_Calendar_API(str_id, i_read_num):
    #SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    if os.path.exists('token.pickle'):
    #{
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    #}
    if not creds or not creds.valid:
    #{
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
    #{
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server()
    #}
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    #}
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    events_result = service.events().list(calendarId = str_id,
                                          timeMin = now,
                                          maxResults = i_read_num,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    
    return events_result.get('items', [])



#**********************************************************
#GoogleCalendarのイベント内容を抽出
#開始時間/終了時間/タイトル/メンバー
#**********************************************************
def read_calendar_now(events, bl_get_room):
    strRTN = ""
    creds = None

    if not events:
        strRTN = 'No upcoming events found.'
    else:
        #for event in events:
        for i0 in range(len(events)):
            event = events[i0]
            
            try:
                strStart = str(event['start'].get('dateTime', event['start'].get('date')))
                strEnd = str(event['end'].get('dateTime', event['end'].get('date')))
                strRTN += 'Start:'
                strRTN += strStart + '\n'
                strRTN += 'End:'
                strRTN += strEnd + '\n'
                strRTN += 'Title:'
                try:
                    strTitle = str(event['summary'])
                    strRTN += strTitle + '\n'
                except:
                    strRTN += '非公開' + '\n'
            except:
                if i < len(events):
                    strRTN += '----------' + '\n'
                pass
            
            
            #-------------------------
            strORG = ''
            strSelf = ''
            cnt_loop = 1
            str_atn_all = ''
            str_atn = ''
            try:
                for i1 in range(len(event['attendees'])):
                    str_atn_all = str(event['attendees'][i1])
                    if str_atn_all.find('organizer') >= 0:
                        str_atn = str(event['attendees'][i1].get('email', event['attendees'][i1].get('string')))
                        strORG += 'Atn0:'
                        strORG += str_atn + '\n'
                    else:
                        str_atn = str(event['attendees'][i1].get('email', event['attendees'][i1].get('string')))
                        if len(str_atn) < 50 and not bl_get_room:
                            #strSelf += 'len = ' + str(len(str_atn))
                            strSelf += 'Atn' + str(cnt_loop) + ':'
                            strSelf += str_atn + '\n'
                            cnt_loop += 1
                    #print(str(event['end'].get('dateTime', event['end'].get('date'))))
                    #print(str(event['attendees'][0].get('email', event['attendees'][0].get('string'))))
                    #print(str(event['attendees']))
            except:
                pass
            
            strRTN += strORG
            strRTN += strSelf
            if i0 < len(events):
                strRTN += '----------' + '\n'
    return strRTN


#**********************************************************
def data_Arrenge(str_data):
    strRTN = ''
    strSerchWord = ''

#**********************************************************
def mDataTypeChange_Ary(str_data):
    Val = str_data
    strSetSplitWord = '----------'
    aryVal = Val.split(strSetSplitWord)
    iSetNum = len(aryVal)
    print(str(len(aryVal)))
    

    ary_strRTN = [iSetNum] * 100
    
    for i in range(iSetNum):
        pass
        
    
#**********************************************************
if __name__ == '__main__':
    room1_val = ''
    room2_val = ''
    room3_val = ''
    iNum = 3
    
    cl_id = 'skydisc.jp_3130303935323631313837@resource.calendar.google.com'
    events = set_Calendar_API(cl_id, iNum)
    room1_val = read_calendar_now(events, False)
    print(room1_val)
    #mDataTypeChange_Ary(room1_val)
    
    cl_id = 'skydisc.jp_34313237303839303238@resource.calendar.google.com'
    events = set_Calendar_API(cl_id, iNum)
    room2_val = read_calendar_now(events, False)
    print(room2_val)
    
    cl_id = 'skydisc.jp_3638353434303437393537@resource.calendar.google.com'
    events = set_Calendar_API(cl_id, iNum)
    room3_val = read_calendar_now(events, False)
    print(room3_val)
    
    #cl_id = 'primary'
    #umd_val = read_calendar_now(cl_id, 10)
    #print('umd' + '\n' + umd_val)
    