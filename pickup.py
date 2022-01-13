import json
import requests
import numpy as np
# config.py
import config

api_key = config.HOTPEPPER_API_KEY
restaurant_datas=[]
reccomend = []
hit = 0

def pickup_datas(keyword):
    query = {
        'key': api_key,
        # 'large_area': 'Z094', # 熊本
        'keyword': keyword,
        # 'genre': 'G013', # ラーメン屋
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
            restaurant_datas.append([restaurant['name'], restaurant['open'], restaurant['urls']])
            reccomend = restaurant_datas[np.random.randint(0, len(restaurant_datas))]
            hit = len(restaurant_datas)
        return reccomend, hit


# if __name__ == "__main__":
    # reccomend, hit = pickup_datas("熊本")
    # print(reccomend)
    # print(f"全{hit}店中")
