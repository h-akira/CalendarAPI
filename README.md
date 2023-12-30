# CalendarAPI
## 主な参考文献
- [公式ドキュメント](https://developers.google.com/calendar/api/quickstart/python)

## 環境構築
```
# 任意の場所にて
git clone git@github.com:h-akira/CalendarAPI.git
cd Calendar_API
pip3 install -r requirements.txt
```

## 概要・使用方法
### `add_event.py`
イベント情報が格納された辞書型を要素とするリスト`events`を作る文がpythonの文法で記述されたテキストファイル
（[サンプル](https://github.com/h-akira/Calendar_API/blob/main/sample/input_sample.py)）
をコマンドライン引数で渡し，それをカレンダーに加える．

利用するには有効な`token.json`が必要がある．
初回でこれがない場合は，認証情報を作成して
`crient_secret_${長いやつ}.json`をダウンロードし，
これをオプション`-c`で渡す．すると`token.json`が出力され，
そのままプログラムが継続する．

## リンク
- https://github.com/h-akira/google_api_operator




