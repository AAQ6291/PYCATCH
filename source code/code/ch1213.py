#!C:\Python26\python
# -*- coding: utf8 -*-

import os
import cgi
import cgitb
cgitb.enable()

"""
對於Windows使用者必須要載入msvcrt模組,
不然上傳後的檔案會有問題.
"""
try:
   import msvcrt
   msvcrt.setmode (0, os.O_BINARY)
   msvcrt.setmode (1, os.O_BINARY)
except ImportError:
   pass

print"Content-Type: text/html; charset=utf-8\n"

# 建立form實例
form = cgi.FieldStorage()

# 判斷是否有上傳檔案
if form.has_key("file"):
   filename = form["file"]
else:
   filename = None

if filename.filename:
   
   # 讀取檔案內容
   data = filename.file.read()

   # 為了要支援上傳的檔名支援中文檔案, 所以必須使用decode('utf-8')來解決。
   fn = filename.filename.decode('utf-8')

   # 將檔案寫入c:\\upload\\位置, 並以二進制寫入
   open("c:\\upload\\%s" % (fn), "wb").write(data)

   message = "檔案上傳完畢."
else:
   message = "沒有檔案."

# 回傳訊息
print message
