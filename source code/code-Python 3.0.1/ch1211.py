#!C:\Python30\python
# -*- coding: utf8 -*-

import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")

# 建立form實例
form = cgi.FieldStorage()

print("您選擇的是:",form.getlist("education"),"<br>")
print("您選擇的是:",form.getlist("education")[0])
