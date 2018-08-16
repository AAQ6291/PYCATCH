#!/usr/bin/env python
#coding=cp950

# 載入time模組
import time

# 定義time1元組型態
time1 = (2008, 12, 30, 11, 20, 21, 0, 56, 1)
# 顯示目前的值
print "time1 = ", time1
# 顯示目前的型態
print "型態 = ", type(time1)
print

# 將time1轉換為時間
time1 = time.mktime(time1)
# 輸出轉換後的結果
print "time1 = ", time1
# 顯示目前的型態
print "型態 = ", type(time1)
# 傳入time.localtime()函數
print "time.localtime = ", time.localtime(time1)
print

# 時間計算, time1與time2差了一天
time1 = (2008, 12, 29, 11, 20, 21, 0, 56, 1)
time2 = (2008, 12, 30, 11, 20, 21, 0, 56, 1)

# 使用time.mktime()函數將time1與time2元組型態轉換為時間並計算回傳秒數
print "time2 - time1"
second = time.mktime(time2) - time.mktime(time1)
print "time2 - time1 = ", second, "秒"

# 計算差幾分
print "time2 - time1 = ", second / 60, "分"

# 計算差幾個小時
print "time2 - time1 = ", second / (60*60), "小時"

# 計算差幾天
print "time2 - time1 = ", second / (60*60*24), "天"

