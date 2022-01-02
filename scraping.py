# メッセージをグーグル検索する
# 検索結果から一つを選ぶ
# 選んだ一つLINEに出力する
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

keyword = "ラインからの引数"

url = "'https://www.google.co.jp/search"

req = requests.get(url, params{"q":keyword})
