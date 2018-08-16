#!/usr/bin/env python
#coding=utf-8

# 載入keyword模組
import keyword

key = "isnot"

# 確認這個值是否為keyword
print "isnot 是否為keyword = ",keyword.iskeyword(key)

print "is 是否為keyword = ", keyword.iskeyword("is")

# 輸出Python的關鍵字列表
print keyword.kwlist
