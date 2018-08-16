# 擷取網頁資料內的EMAIL帳號

import requests

url = 'https://www.com.tw/cross/namequery107.html'
html = requests.get(url).text.splitlines()
# 截取前15行
for i in range(0, 55):
    print(html[i])
