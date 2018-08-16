#!/usr/bin/env python
#coding=utf-8

# 載入httplib模組
import httplib

# 載入urllib模組
import urllib

# 使用urllib.urlencode()函數並傳入user與pwd參數
params = urllib.urlencode({'user': "abc", 'pwd': "123"})

# 設定header
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

# 連線網頁
conn = httplib.HTTPConnection("www.python.tw")

# 傳送POST位置到/cgi-bin/login, 接著帶入參數與header
conn.request("POST", "/cgi-bin/login", params, headers)

# 取得回應
response = conn.getresponse()

# 輸出連線狀態 200 OK
print response.status, response.reason

data = response.read()
conn.close()
