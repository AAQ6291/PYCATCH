#!C:\Python30\python
# -*- coding: utf8 -*-

import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")

# 建立form實例
form = cgi.FieldStorage()

# 判斷傳遞過來的值是否有username變數
if form.has_key("username"):
   username = form["username"].value
else:
   username = None

# 判斷傳遞過來的值是否有password變數   
if form.has_key("password"):
   password = form["password"].value
else:
   password = None

if username and password:
   print("<h2>您輸入的帳號: %s</h2>" % (username))
   print("<h2>您輸入的密碼: %s</h2>" % (password))
else:
   print("<h2>帳號或密碼未填寫.</h2>")
