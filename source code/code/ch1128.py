#!/usr/bin/env python
#coding=utf-8

# 載入imghdr
import imghdr

# 使用imghdr.what()函數去識別影像檔案
result = imghdr.what("./ch1102.jpg")

# 傳回檔案型態
print "ch1102.jpg 檔案類型 = ", result

# 接著我們嘗試將ch1102.jpg附檔名改為.txt試圖要去欺騙imghdr.what()函數
result = imghdr.what("./ch1102.txt")

# 傳回檔案型態
print "ch1102.txt 檔案類型 = ", result
