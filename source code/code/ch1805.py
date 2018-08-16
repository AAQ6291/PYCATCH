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

# 取得頁面內容
doc = app.Document

# 等待取得內容的狀態為"完成"
while doc.readyState != "complete":
   time.sleep(2)

"""
f是表單名稱<form name ="f"> q是欄位名稱<input name="q">
在這個欄位輸入要搜尋的內容
"""
doc.f.q.value = "python"

# 送出表單
doc.f.submit()

