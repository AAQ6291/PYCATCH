# 擷取網頁資料

import requests

url = 'https://www.most.gov.tw/folksonomy/list?menu_id=d646fba1-72d2-4040-881a-8efd7dafcfb6&l=ch&view_mode=listView'
html = requests.get(url).text.splitlines()
# 截取前15行
for i in range(0, 15):
    print(html[i])
