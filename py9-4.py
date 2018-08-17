# Beautifulsoup 4 基本使用方式
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = 'http://www.timeanddate.com/weather'
domain = "{}://{}.".format(urlparse(url).scheme, urlparse(url).hostname)

html = requests.get(url).text
sp = BeautifulSoup(html, "html.parser")

# 傳回所有符合條件的內容 -- 抓取<a>標籤 或是多個標籤
links = sp.find_all('a')
all_links = sp.find_all(['a', 'img'])
# 列出所有抓取元素之總數
print(len(links), "個元素!")
print(len(all_links), "個元素!")
# 列出所有抓取元素之內容
lmax = len(links)
i = 0
while i < lmax:
    print('(單一)ID', i, '--Content:', links[i].contents,
          '| href:', links[i].get("href"))
    i += 1
# 多個條件, 去除空屬性之元素並檢查是否為完整網址
for lk in all_links:
    src = lk.get('src')
    href = lk.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'):
                print('多個條件--<a>', t)
            else:
                print('多個條件--<img>', domain+t)
