#!/usr/bin/env python3

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gmail_quickstart]
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# rom googleapiclient.errors import HttpError
####################
import base64
# from email.message import EmailMessage
####################

# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
## SCOPES = ['https://mail.google.com/']
## SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SCOPES = ['https://www.googleapis.com/auth/calendar']
## SCOPES = ['https://calendar.google.com/']

def get_creds(token_json='token.json',credentials_json='credentials.json'):
  # アクセストークンを取得
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists(token_json):
    creds = Credentials.from_authorized_user_file(token_json, SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(credentials_json, SCOPES)
      creds = flow.run_local_server(port=0)
    # Save the credentials for tahe next run
    with open(token_json, 'w') as token:
      token.write(creds.to_json())    
  return creds

def get_service(creds):
  try:
    service = build('calendar', 'v3', credentials=creds)
  except:
    print("Couldn't get service.")
    service = None
  return service

def sample():
  import argparse
  parser = argparse.ArgumentParser(description="""\
イベントを10件取得する．
""")
  parser.add_argument("--version", action="version", version='%(prog)s 0.0.1')
  parser.add_argument("-t", "--token", metavar="Path", default=os.path.join(os.path.dirname(__file__),"../secret/token.json"), help="token.json（存在しない場合は生成される）")
  parser.add_argument("-c", "--credentials", metavar="Path", default=os.path.join(os.path.dirname(__file__),"../secret/credentials.json"), help="credentials.json（client_secret_hogehoge.json）")
  options = parser.parse_args()
  N=10
  creds = get_creds(options.token,options.credentials)
  service = get_service(creds)
# Call the Calendar API
  import datetime
  now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
  print('Getting the upcoming 10 events')
  events_result = service.events().list(calendarId='primary', timeMin=now,maxResults=N, singleEvents=True,orderBy='startTime').execute()
  events = events_result.get('items', [])
  if not events:
    print('No upcoming events found.')
    return

  # Prints the start and name of the next 10 events
  for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])

if __name__ == '__main__':
  sample()
