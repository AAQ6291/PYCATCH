#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入MySQLdb模組與MySQLdb.cursors模組
import MySQLdb
import MySQLdb.cursors

"""
建立MySQL連線
host = 主機IP
port = 主機PORT
user = 登入帳號
passwd = 登入密碼
compress = 壓縮傳輸
"""
db = MySQLdb.connect(
   host='localhost',
   port=3306,
   user='python',
   passwd='1234',
   compress=True)

# 選擇資料庫
db.select_db('Python')

# 建立cursor類別
c = db.cursor()

# 定義SQL語法
SQL = """
DELETE FROM employee WHERE ID='3';
"""

# 執行SQL
db.query(SQL)

# 提交SQL
db.commit()

# 關閉連線
db.close()
