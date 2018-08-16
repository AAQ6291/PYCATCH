# -*- coding: cp950 -*-
import urllib
import htmllib
import formatter

class SearchLinks(htmllib.HTMLParser):
   def __init__(self, formatter) :
      htmllib.HTMLParser.__init__(self, formatter)
      self.links = []

   # 覆載（override）原本的start_a　method
   def start_a(self, attrs):
      if len(attrs) > 0:
         for attr in attrs:
            if attr[0] == "href":
               self.links.append(attr[1])

   def get_links(self):
      return self.links

# 建立formatter.NullFormatter實例（instance）
f = formatter.NullFormatter()

# 建立SearchLinks()實例（instance）
html_parser = SearchLinks(f)

# 讀取網頁
data = urllib.urlopen("http://www.google.com")

# 將網頁內容傳入feed()函數
html_parser.feed(data.read())

# 關閉html_parser
html_parser.close()

# 搜尋網頁內所有<a href="*">網址
links = htmlparser.get_links()

# 輸出
i=0
for link in links:
   print i, link
   i+=1

