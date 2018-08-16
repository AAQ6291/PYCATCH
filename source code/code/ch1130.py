#!/usr/bin/env python
#coding=utf-8

# 載入linecache模組
import linecache

filename = "./ch205.txt"

# 輸出檔案的第2行
print linecache.getline(filename,2)

# 輸出檔案的第5行
print linecache.getline(filename,5)
