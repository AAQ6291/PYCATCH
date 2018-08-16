#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bsddb

# 建立一個資料庫, 名稱為 database.db
db = bsddb.btopen("./databse.db", "c")

# 寫入多筆測試資料到資料庫裡
for x in range(10):
   db["%d" % (x)] = "%d" % (x*x)

# 取出第5筆資料
print db['5']

# 輸出存在資料庫內的所以keys值
print db.keys()

# 跳到第一筆
print "第一筆", db.first()

# 跳到下一筆
print "下一筆", db.next()

# 跳到下一筆
print "下一筆", db.next()

# 跳到下一筆
print "下一筆", db.next()

# 跳到最後一筆
print "最後一筆", db.last()

# 直接跳到指定的筆數
print "直接跳到指定的筆數", db.set_location('5')

# 上一筆
db.previous()
print "上一筆", db.previous()

# 輸出資料庫內的所有資料
for x, y in db.iteritems():
   print x, y
   
print "'6'是否有在資料庫內", ('6' in db)

# 將資料庫的資料存到檔案內
db.sync()

# 關閉
db.close()
