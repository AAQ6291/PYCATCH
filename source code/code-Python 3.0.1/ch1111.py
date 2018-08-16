#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入calendar模組
import calendar

"""
指定每週的第一天是星期一, 預設的第一天是星期日,
HTMLCalendar()函數是指定產生HTML格式的日曆
"""
hc = calendar.HTMLCalendar(calendar.MONDAY)

# 指定要產生日曆的年月與月份
html = hc.formatmonth(2009, 12)

# 產生的結果儲存成ch1111.html
f = open("./ch1111.html", "w")
f.write(html)
f.close()

