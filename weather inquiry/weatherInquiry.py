# 必須提前利用 buildCityData.py 建立城市碼的資庫料(city_data.pkl)才能查詢中國天氣

import urllib.request
import json
import pickle
import gzip

pickle_file = open('D:\\WorkTmp\\projTest\\LearnPython\\city_data.pkl', 'rb')
city = pickle.load(pickle_file)

password = input('中國天氣查詢，請輸入中國城市(字體：繁體中文)：')
name1 = city[password]

url = 'http://wthrcdn.etouch.cn/weather_mini?citykey=' + name1

## 查看Content-Type、Content-Encoding以及其他資訊
#headers = urllib.request.urlopen(url).getheaders()
#print('\n' + headers + '\n')

data = urllib.request.urlopen(url).read()
data = gzip.decompress(data).decode('utf-8')

## 查看內容
#print('\n' + data + '\n')

weatherInfo = json.loads(data)
weatherInfoDetail = dict(weatherInfo['data']['forecast'][0])

print('\n')
print('城市：' + weatherInfo['data']['city'])
print('時間：' + weatherInfoDetail['date'])
print('溫度：' + weatherInfo['data']['wendu'])
print('高溫：' + weatherInfoDetail['high'].replace('高温 ', ''))
print('低溫：' + weatherInfoDetail['low'].replace('低温 ', ''))
print('風向：' + weatherInfoDetail['fengxiang'])
print('雲層：' + weatherInfoDetail['type'])
print('提醒：' + weatherInfo['data']['ganmao'])

print('\n')

## 寫檔，查看格式
#weatherJSON = json.JSONDecoder().decode(data)
#with open('D:\\WorkTmp\\projTest\\LearnPython\\dataJson.txt', 'w', encoding='utf-8') as f:
#    json.dump(weatherJSON, f, ensure_ascii=False)

input('按 ENTER 退出')

