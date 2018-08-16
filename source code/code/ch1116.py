#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbhash

# 使用dbhash建立資料庫
db = dbhash.open("./database.db", "c")

# 新增一筆資料
db["www.msn.com"] = "msn site"

# 關閉資料庫
db.close()

# 讀取資料庫內容
db = dbhash.open("./database.db", "r")

# 輸出資料庫內容
for x in db.keys():
   print x

db.close()
