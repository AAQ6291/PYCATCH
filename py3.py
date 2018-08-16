# 解析網址 範例
from urllib.parse import urlparse

uc = urlparse('https://tw.stock.yahoo.com/new_list/d/e/N1.html?q=&pg=4')
print('解析結果 -- ', uc)
print('解析網址 -- ', uc.netloc)
print('解析路徑 -- ', uc.path)
print('解析查詢條件 -- ', uc.query)
