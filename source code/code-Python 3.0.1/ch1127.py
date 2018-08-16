#!/usr/bin/env python
#coding=utf-8

# 載入http.client模組
import http.client

# 載入urllib模組
import urllib.parse

# 使用urllib.parse.urlencode()函數並傳入user與pwd參數
params = urllib.parse.urlencode({'user': "abc", 'pwd': "123"})

# 設定header
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

# 連線網頁
conn = http.client.HTTPConnection("www.python.tw")

# 傳送POST位置到/cgi-bin/login, 接著帶入參數與header
conn.request("POST", "/cgi-bin/login", params, headers)

# 取得回應
response = conn.getresponse()

# 輸出連線狀態 200 OK
print(response.status, response.reason)

data = response.read()
conn.close()
