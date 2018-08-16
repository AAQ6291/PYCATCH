#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入datetime
import datetime

# 取得目前時間並傳遞值給now變數
now = datetime.datetime.now()

# 取出date給date變數
date = now.date()

# 取出時間給time變數
time = now.time()

print date
print time

# 我們可以使用datetime.combine()函數來合併時間與日期
d = datetime.datetime.combine(date, time)

print type(d)

print d
