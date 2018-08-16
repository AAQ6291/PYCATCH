#!/usr/bin/env python
# -*- coding: utf-8 -*-

import anydbm

print "open database"
# 建立資料庫, 名稱為database.db
db = anydbm.open("database.db", "c")

db["www.yahoo.com"] = "Yahoo 搜尋引擎"
db["www.google.com"] = "Google 搜尋引擎"

# 輸出資料庫內容
for x, y in db.iteritems():
   print x, y

# 關閉資料庫
db.close()
print "close database"

print "open database"
# 再次開啟資料庫
db = anydbm.open("database.db", "w")

# 輸出資料庫內容
for x, y in db.iteritems():
   print x, y

# 關閉資料庫
db.close()
print "close database"

