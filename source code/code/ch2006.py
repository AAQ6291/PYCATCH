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

# 建立cursor類別
c = db.cursor()

# 定義SQL語法
SQL = """
SELECT * FROM employee;
"""

# 執行SQL
c.execute(SQL)

# 取出結果
result = c.fetchall()

# 逐筆輸出
for row in result:
   print row[0], row[1], row[2], row[3], row[4], row[5]

# 取得取出資料的筆數
print "共:" +str(len(result))+ "筆"

# 結束cursor
c.close()

# 關閉連線
db.close()
