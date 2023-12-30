#!/usr/bin/env python3
import os
import sys
import datetime
import google.auth
import traceback
from google_api_operator.authentication import get_service
from google_api_operator.gcalendar import SCOPES

def main():
  import argparse
  parser = argparse.ArgumentParser(description="""\
カレンダーにイベントを追加する．
""")
  parser.add_argument("--version", action="version", version='%(prog)s 0.0.1')
  parser.add_argument("-t", "--token", metavar="Path", default=os.path.join(os.path.dirname(__file__),"../secret/token.json"), help="token.json（存在しない場合は生成される）")
  parser.add_argument("-c", "--credentials", metavar="Path", default=os.path.join(os.path.dirname(__file__),"../secret/credentials.json"), help="credentials.json（client_secret_hogehoge.json）")
  parser.add_argument("--log", metavar="ファイル", help="実行履歴をファイルに追記する．")
  parser.add_argument("file", metavar="file", help="イベント情報が格納された辞書型を要素とするリスト「events」\
を作る文がpythonの文法で記述されたテキストファイル")
  options = parser.parse_args()

  if options.log:
    start = datetime.datetime.now()
    options_str = " ".join([i for i in sys.argv[1:]])

  try:
    service = get_service(SCOPES, options.credentials, options.token, "calendar", "v3")
  except google.auth.exceptions.RefreshError:
    print(f"認証情報が無効です．{options.token}を削除してください．")
    traceback.print_exc()
    sys.exit()

  events=[]
  with open(options.file, mode='r') as f:
    exec(f.read())
  for event in events:
    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))

  if options.log:
    end = datetime.datetime.now()
    with open(options.log, mode='a') as f:
      print("start time: {}".format(start.strftime("%Y-%m-%d--%H-%M-%S")),file=f)
      print("end time  : {}".format(end.strftime("%Y-%m-%d--%H-%M-%S")),file=f)
      print("options   : {}".format(options_str),file=f)

if __name__ == "__main__":
  main()



