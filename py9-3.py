# 擷取網頁資料內的EMAIL帳號

import requests
import re  # 正則表達式的模組

regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
# 基于隐私，使用了“XXXXXXXXXXXXXX”
url = 'http://www.liveabc.com/index.asp'
html = requests.get(url).text
# print(html)
emails = re.findall(regex, html)
i = 0
for email in emails:
    i += 1
    if i < 16:
        print("{} :{}".format(i, email))
