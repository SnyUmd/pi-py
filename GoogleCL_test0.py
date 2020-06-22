
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


#***************************************************
str_me = 'primary'
str_kaigi1 = 'skydisc.jp_3130303935323631313837@resource.calendar.google.com'
str_kaigi2 = 'skydisc.jp_34313237303839303238@resource.calendar.google.com'
str_kaigi3 = 'skydisc.jp_3638353434303437393537@resource.calendar.google.com'

#Select
str_cl_id = str_me 
#str_cl_id = str_kaigi1 
#str_cl_id = str_kaigi2
#str_cl_id = str_kaigi3
#****************************************************



def main():
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

    if str_cl_id == str_kaigi1:
        print('◆会議室1')
    elif str_cl_id == str_kaigi2:
        print('◆会議室2')
    elif str_cl_id == str_kaigi3:
        print('◆会議室3')

    print(str_cl_id)

    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId=str_cl_id,
                                          timeMin=now,
                                          maxResults=10, 
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()