import urllib.request
import urllib.error
import time
import socket
import random

socket.setdefaulttimeout(20)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept-Encoding':'*',
    'Connection':'keep-alive'
}

iplist = [
    '124.156.108.71:82',
    '119.41.236.180:8010',
    '139.196.78.83:80',
    '101.231.104.82:80',
]

#url = 'https://www.whatismyip.com.tw/'
url = 'http://www.j4.com.tw/james/remoip.php'

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0')]

urllib.request.install_opener(opener)

req = urllib.request.Request(url, headers=headers)

try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    response.close()
except urllib.error.URLError as e:
    print(e.reason)

time.sleep(1)

print(html)
