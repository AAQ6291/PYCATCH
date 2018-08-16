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
CREATE TABLE employee(
       ID int(10) NOT NULL auto_increment,
       FirstName varchar(12),
       LastName varchar(12),
       Gender char(1),
       Email varchar(60),
       Tel varchar(12),
       PRIMARY KEY ID(ID)
);
"""

"""
執行SQL語法建立資料表,
如果資料表已經存在就會回傳 db.OperationalError例外.
"""
try:
   db.query(SQL)
except db.OperationalError:
   print("資料表已經存在")

