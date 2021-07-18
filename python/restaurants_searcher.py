# restaurants_searcher.py

import json
import csv
import requests

# 初期設定
KEYID = "491d372caaee763b"
COUNT = 100
PREF = "Z011"
FREEWORD = "野方駅"
FORMAT = "json"

#パラメータ設定
PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}

def write_data_to_csv(params):
    restaurants = [["名称","営業日","住所","アクセス"]]
    json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params).text
    response = json.loads(json_res)
    if "error" in response["results"]:
        return print("エラーが発生しました！")
    for restaurant in response["results"]["shop"]:
        rest_info = [restaurant["name"], restaurant["open"], restaurant["address"], restaurant["access"]]
        restaurants.append(rest_info)
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(restaurants)
    return print(restaurants)

write_data_to_csv(PARAMS)