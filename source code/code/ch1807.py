#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入win32com.client模組
import win32com.client
import time

# 建立IE物件
app = win32com.client.Dispatch("InternetExplorer.Application")

# 顯示IE瀏覽器
app.Visible = 0

# 開啟網頁
app.Navigate("http://www.google.com.tw")

# 等待網頁開啟
while app.ReadyState != 4:
   time.sleep(2)

# 只有取得頁面內容的文字
text = app.Document.body.innerText
# Unicode轉換
text = unicode(text)

# 結束程式
app.Quit()

#輸出抓取結果
print(text)
