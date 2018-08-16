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

# 執行SQL語法並插入多筆資料
try:
   c.executemany(
      """
      INSERT INTO employee (
             ID, FirstName, LastName, Gender, Email, Tel)
             VALUES (
             null, %s, %s, %s, %s, %s)""",
      [
         ('JHIH WEI', 'GUO', 'M', 'jhihwel@gmail.com', '22334455'),
         ('JIAN HONG', 'WANG', 'M', 'jianhong@gmail.com', '23456677'),
         ('PEI JYUN', 'CHEN', 'F', 'peijyun@gmail.com', '22345678'),
         ('JIA YING', 'HU', 'F', 'jiaying@gmail.com', '23875432')]
      )   
except db.IntegrityError:
   print("重複Key值")

# 執行 commit()函數提交SQL
db.commit()
