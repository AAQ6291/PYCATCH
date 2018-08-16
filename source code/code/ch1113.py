#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

# 我們可以利用datetime.datetime手動設定時間
now = datetime.datetime(2008,12,16,18,1,20)

# 輸出手動設定的時間
print now

# 呼叫now變數裡面的屬性
print now.year, now.month, now.day

# 呼叫now變數裡面的屬性
print now.hour, now.minute, now.second
