#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入win32com.client模組
import win32com.client
import time

# 建立IE物件
app = win32com.client.Dispatch("InternetExplorer.Application")

# 顯示IE瀏覽器
app.Visible = 1

app.Navigate("http://www.google.com")

# 等待網頁開啟
while app.ReadyState != 4:
   time.sleep(2)

# 取得網頁內的連結URL
try:   
   for link in app.Document.links:
      print link
except:
   pass
