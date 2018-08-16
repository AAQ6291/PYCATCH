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

# SQL語法
SQL = """
CREATE DATABASE `Python`;
"""

"""
執行SQL語法建立資料庫,
如果資料庫已經存在就會回傳 db.ProgrammingError例外.
"""
try:
   db.query(SQL)
except db.ProgrammingError:
   print("資料庫已經存在")
