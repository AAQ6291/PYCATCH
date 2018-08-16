#!C:\Python26\python
# -*- coding: utf8 -*-

import cgi
import cgitb
cgitb.enable()

print"Content-Type: text/html; charset=utf-8\n"

# 建立form實例
form = cgi.FieldStorage()

# 輸出多選項目內容
print "您選擇的是:",form.getlist("interest"),"<br>"

# 逐步輸出選擇的項目
print "您選擇的是:"
for select in form.getlist("interest"):
   print select
