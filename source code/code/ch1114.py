#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, time

# 直接取得系統時間
now = datetime.datetime.now()

# 輸出目前系統時間
print now

# C standard
print now.ctime()

# ISO 8601 format
print now.isoformat()

# 指定時間輸出的格式
print now.strftime("%Y/%m/%d %H:%M:%S")


