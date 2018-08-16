#!/usr/bin/env python
#coding=utf-8

# 載入http.client模組
import http.client

# 建立連線
conn = http.client.HTTPConnection('www.google.com.tw')

# 請求網頁名稱
conn.request("GET", "/index.html")

# 請求伺服端回應
read_one = conn.getresponse()

# 輸出連線狀態與連線狀態碼
print(read_one.status, read_one.reason)

# 關閉連線
conn.close()

# 請求網頁名稱
conn.request("GET", "http://news.google.com.tw/nwshp?hl=zh-TW&tab=wn")

# 請求伺服端回應
read_two = conn.getresponse()

# 輸出連線狀態與連線狀態碼
print(read_two.status, read_two.reason)

# 關閉連線
conn.close()
