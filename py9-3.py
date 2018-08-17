# 擷取網頁資料內的EMAIL帳號
# 參考 "Python網路爬蟲與資訊提取（三）—— Re模組" -- https://ppt.cc/falmkx

import requests
import re  # 正則表達式的模組

# email正規表示法: abaaxxx@xxgmail.xxxcom
# 字串符號「"」之前的「r」是讓Python直譯器知道在其後的字串內容,請保留原來的樣子,不要做任何的解譯動作。
regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"

url = 'http://www.liveabc.com/index.asp'
html = requests.get(url).text

# re.findall() -- 搜字串,以列表型別返回全部能匹配的字串
emails = re.findall(regex, html)
i = 0
for email in emails:
    i += 1
    if i < 16:
        print("{} :{}".format(i, email))
