#!/usr/bin/env python
#coding=utf-8

import time

# 定義日期變數, 給下面的函數使用
now = time.localtime(time.time())
year, month, day, hour, minute, second, weekday, yearday, daylight = now

# 定義showdate()函數, 顯示年月日
def showdate():
    return "%04d-%02d-%02d" % (year, month, day)

# 定義showtime()函數, 顯示時間
def showtime():
    return "%02d:%02d:%02d" % (hour, minute, second)

# 定義showweek()函數, 顯示今天星期幾.
def showweek():
    return ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")[weekday]

# 將函數設為date序列內的項目元素
date = [showdate(),showtime(),showweek()]

# 呼叫 showdate()函數
print "今天日期:", date[0]

# 呼叫 showtime()函數
print "現在時刻:", date[1]

# 呼叫 showweek()函數
print "今天星期:", date[2]

# 新增加一個函數, 這個函數是在顯示今天是今年的第幾天.
def showday():
    return yearday

# 將新增加的函數加入date序列內
date.append(showday())

# 呼叫 showday()函數
print "今天是今年的第幾天:", date[3]

# 呼叫date序列
print date


