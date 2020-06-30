#from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

str_cl_id = 'primary'
strReturn = ''
numEvents = 5

#**********************************************************
def mFileWrite_text(str_filename, str_html_text):
    strNL = '\n'
    str_html_val = '<html>' + strNL + \
                    '<body>' + strNL + \
                    str_html_text + strNL + \
                    '</body>' + strNL + \
                    '</html>'
    #str_html_val.encode('shift_jis')
    str_html_val.encode('utf-8')
    #print(str_html_val)
    f = open(str_filename, 'w')
    f.write(str_html_val)
    f.close()


cntTest = 0


def main():
    global strReturn
    
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    strReturn += now# + ','
    strReturn += "\r\n"
    
    dt_time_min = "2020-06-19T00:00:00.000000Z"
    #dt_time_min = str(datetime.date.today()) + "T00:00:00.000000Z"
    #print(str(dt_time_min))

    #print('Getting the upcoming 10 events')
    strReturn += str(numEvents)
    strReturn += 'events'# + ','
    events_result = service.events().list(calendarId=str_cl_id,
                                          timeMin=dt_time_min,
                                          maxResults=numEvents, 
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    strReturn += "\r\n"


    strReturn += "-----------------------" + "\r\n"

    strSummary = ""

    if not events:
        strSummary = 'No upcoming events found.'
    for event in events:
        
        #予定のタイトルを取得
        strSummary= str(event['summary']) + "\r\n"
        
        #主催者を取得
        #print(str(event['organizer'].get('email', event['organizer'].get('email'))) + "\r\n")
        #メンバーを取得
        #※メンバーには主催者も含まれている。
        #print(str(event['attendees'][0].get('email', event['attendees'][0].get('email'))) + "\r\n")
        
        #メンバー数を表示
        #（※作成者以外でメンバーがいない時、attendessは参照エラーとなる。）
        #print(str(len(event['attendees'])))

        #時間情報を取得
        start = str(event['start'].get('dateTime', event['start'].get('date')))[0:16] + "\n"
        strEnd = str(event['end'].get('dateTime', event['end'].get('date')))[0:16] + "\n"
        
        #=＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
        #メンバーを取得するループ
        strORG = ''
        strSelf = ''
        str_atn_all = ''
        str_atn = ''
        try:
            for i1 in range(len(event['attendees'])):
                str_atn_all = str(event['attendees'][i1])
                #主催者であるかを判定
                if str_atn_all.find('organizer') >= 0:
                    #主催者のときは先頭に「＊」をつける
                    #主催者のディスプレイ名を取得
                    str_atn = str(event['attendees'][i1].get('displayName', event['attendees'][i1].get('displayName')))
                    #ディスプレイ名が無ければ、メールアドレスに
                    if(str_atn == 'None'):
                        str_atn = str(event['attendees'][i1].get('email', event['attendees'][i1].get('email')))
                    #strORG += 'Atn0:'
                    strORG += '*'
                    strORG += str_atn + '\n'
                else:
                    #メンバーのディスプレイ名を取得
                    str_atn = str(event['attendees'][i1].get('displayName', event['attendees'][i1].get('displayName')))
                    #ディスプレイ名が無ければ、メールアドレスに
                    if(str_atn == "None"):
                        str_atn = str(event['attendees'][i1].get('email', event['attendees'][i1].get('email')))
                    strSelf += str_atn + '\n'
        except:
            pass
        #=＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

        strReturn += strSummary# + "\n"
        strReturn += start# + "\n"
        strReturn += strEnd# + "\n"
        strReturn += strORG# + "\n"
        strReturn += strSelf# + "\n"
        strReturn += "-----------------------" + "\r\n"

    print(strReturn)

    strFileName = "/mnt/chromeos/removable/SD256/_py/__github/pi-py-master/google_calendar/0012/index.html"
    #改行コードをhtml改行コードに変換
    strReturn = strReturn.replace('\n', '<br />')
    mFileWrite_text(strFileName, strReturn)


if __name__ == '__main__':
    main()