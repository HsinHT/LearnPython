import urllib.request
import urllib.parse
import json

# 請求URL：'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'，必須刪除 ? 前的 _o 才能正常執行，不然會出錯({"errorCode":50})。

content = input('Enter the words needs translated: ')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

'''
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
'''

data = {}

data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15707889602430'
data['sign'] = 'e0086b9e063a3757b87018ad11242436'
data['ts'] = '1570788960243'
data['bv'] = 'e2a78ed30c66e16a857c5b6486a1d326'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('utf-8')

'''
req = urllib.request.Request(url, data, head)
'''

req = urllib.request.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0')

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

target = json.loads(html)

print('翻譯結果：%s' % (target['translateResult'][0][0]['tgt']))

