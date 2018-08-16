#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入MySQLdb模組
import MySQLdb

"""
建立MySQL連線
host = 主機IP
port = 主機PORT
user = 登入帳號
passwd = 登入密碼
"""
db = MySQLdb.connect(host='localhost', port=3306, user='python', passwd='1234')

# 回傳連線狀態
print(db.stat())

# 關閉連線
db.close()
