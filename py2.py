import urllib.request
import urllib.parse
from urllib.request import urlopen
from urllib.parse import urlparse

#
url = 'https://news.google.com/?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'
html = urlopen(url)

data = html.read()
data = data.decode('UTF-8')
print('Header 資訊:', html.info())
print("-- 網頁狀態碼 -- \n", html.getcode())
#
url = 'http://pythonprogramming.net'
values = {'S': 'basic', 'submit': 'search'}
data = urllib.parse.urlencode(values)
data = data.encode('UTF-8')
req = urllib.request.Request(url, data)
resp = urlopen(req)
respData = resp.read()
print(respData)
#
