# このファイルはテキストして読み込まれてexec()関数で実行される．
# 空のリスト`events=[]`は宣言済みで，これに対してイベント情報の辞書型をappendする．
# templates.pyをimportして利用できる．各関数は辞書型を返す．
### Usage of templates ###
# events.append(tempalates.basic(タイトル，開始時刻[datetime型]，終了時刻[同]，
# location=場所，description=説明，colorId=カラー[0から11，str可], timeZone=タイムゾーン[デフォルトはJapan]))

### Sample ###
from google_api_operator.gcalendar import templates
from datetime import datetime as dt
events.append(templates.basic("テスト1",dt(2022,11,6,11,00),dt(2022,11,6,13,00)))
events.append(templates.basic("テスト2",dt(2022,11,7,11,00),dt(2022,11,7,13,00),colorId=4))
