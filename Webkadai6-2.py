import requests
import json

area_code = "120000"
url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"

response = requests.get(url)

if response.status_code == 200:
    forecast_data = response.json()

    time_series = forecast_data[0]["timeSeries"][0]
    time_defs = time_series["timeDefines"]
    weathers = time_series["areas"][0]["weathers"]

    for i in range(len(time_defs)):
        print(f"{time_defs[i]}: {weathers[i]}")
else:
    print("取得できませんでした:")

#参照オープンデータ名(気象庁 天気予報API（JSON形式）)
#概要(国の都道府県単位での天気予報（今日・明日など）)
#エンドポイントは https://www.jma.go.jp/bosai/forecast/data/forecast/{地域コード}.json
#機能は実行すると千葉県の日付と天気予報を教えてくれる。

