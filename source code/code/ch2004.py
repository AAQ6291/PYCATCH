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

# 選擇資料庫
db.select_db('Python')

# SQL語法
SQL = """
INSERT INTO employee (
       ID, FirstName, LastName, Gender, Email, Tel)
       VALUES (
       null, 'SIN YI', 'LIN', 'F', 'sinyi@gmail.com', '23456789'
       );

"""

# 建立cursor類別
c = db.cursor()

# 執行SQL語法
try:
   c.execute(SQL)   
except db.IntegrityError:
   print("重複Key值")

# 執行 commit()函數提交SQL
db.commit()
