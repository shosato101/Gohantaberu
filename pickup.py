import json
import requests
import numpy as np
# config.py
import config

api_key = config.HOTPEPPER_API_KEY
class Reccomend(object):

    def __init__(self, keyword):
        self.keyword = keyword
        self.restaurant_datas = []
        self.suggest = ""
        self.hit = 0

    def pickup_datas(self):
    
        query = {
            'key': api_key,
            # 'large_area': 'Z094', # 熊本
            'keyword': self.keyword,
            #  'genre': 'G001', # 居酒屋
            # 'lunch': 1, #ランチありのみ
            'order': 1, #名前の順
            'start': 1, #検索結果の何番目から出力するか
            'count': 100, #最大得件数
            'format': 'json'
        }
        url_base = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
        responce = requests.get(url_base, query)
        result = json.loads(responce.text)['results']['shop']

        if len(result) == 0:
            reccomend = "ありません"
            return reccomend

        else:
            for restaurant in result:
                self.restaurant_datas.append([restaurant['urls']])

            self.suggest = self.restaurant_datas[np.random.randint(0, len(self.restaurant_datas))]
            self.hit = len(self.restaurant_datas)
            reccomend = f"{self.suggest}\n全{self.hit}件中"
            return reccomend
