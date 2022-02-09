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
            'large_area': 'Z094', # 熊本
            # 'address': self.keyword,
            # 'genre': 'G014', # 居酒屋
            'keyword': self.keyword,
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
                self.restaurant_datas.append([restaurant['name'], restaurant['address'], restaurant['open'], restaurant['urls']])

            self.suggest = self.restaurant_datas[np.random.randint(0, len(self.restaurant_datas))]
            restaurant_name = self.suggest[0]
            restaurant_address = self.suggest[1]
            restaurant_open = self.suggest[2]
            restaurant_urls = self.suggest[3]["pc"]
            self.hit = len(self.restaurant_datas)
            reccomend = f"【{restaurant_name}】\n\n{restaurant_address}\n\n［{restaurant_open}］)\n\n{restaurant_urls}\n\n\n全{self.hit}件中"
            return reccomend
