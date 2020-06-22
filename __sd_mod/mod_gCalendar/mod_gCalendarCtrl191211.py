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
#SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


#**********************************************************
#GoogleCalendarAPI　SET
#**********************************************************
def set_Calendar_API(str_id, i_read_num):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
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
            
            p0 = 0
            p1 = 0
            str_replace = ''
            try:
                try:
                    strTitle = str(event['summary'])
                    strRTN += strTitle + '\n'
                except:
                    strRTN += '非公開' + '\n'
                    
                strStart = str(event['start'].get('dateTime', event['start'].get('date')))[0:16]
                ##+++++++++++++++++++++++++++++
                #strStart = time_Arrenge(strStart)
                strStart = time_Arrenge2(strStart)
                
                strEnd = str(event['end'].get('dateTime', event['end'].get('date')))[0:16]
                strEnd = time_Arrenge2(strEnd)
                #strRTN += 'Start:'
                strRTN += strStart + '\n'
                #strRTN += 'End:'
                strRTN += strEnd + '\n'
                #strRTN += 'Title:'
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
                        #strORG += 'Atn0:'
                        strORG += '*'
                        strORG += str_atn + '\n'
                    else:
                        str_atn = str(event['attendees'][i1].get('email', event['attendees'][i1].get('string')))
                        if len(str_atn) < 50 and not bl_get_room:
                            #strSelf += 'len = ' + str(len(str_atn))
                            #strSelf += 'Atn' + str(cnt_loop) + ':'
                            strSelf += str_atn + '\n'
                            cnt_loop += 1
                    #print(str(event['end'].get('dateTime', event['end'].get('date'))))
                    #print(str(event['attendees'][0].get('email', event['attendees'][0].get('string'))))
                    #print(str(event['attendees']))
            except:
                pass
            
            strRTN += strORG
            strRTN += strSelf
            if i0 < len(events) - 1:
                strRTN += '----------' + '\n'
    return strRTN


#**********************************************************
#時間補正　17時間少ない時間で取得されるので補正
#str_time:YYYY-mm-ddTHH:MM
#17時間プラスして返す
#**********************************************************
def time_Arrenge2(str_time):
    strRTN = str_time
    strRTN = strRTN.replace('T', ' ')
    dateVal = datetime.datetime.strptime(strRTN, '%Y-%m-%d %H:%M')
    dateVal = dateVal + datetime.timedelta(hours=17)
    return dateVal.strftime('%Y-%m-%d %H:%M:%S')[0:16]


 
set_Calendar_API('skydisc.jp_3130303935323631313837@resource.calendar.google.com', 5)
    