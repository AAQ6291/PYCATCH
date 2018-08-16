#!/usr/bin/env python
#coding=utf-8

## Python 2.6新增的功能，載入__future__模組去關閉print陳述式後開啟print()函數。
from __future__ import print_function
import datetime

f=open("C:\\today.txt","w+")
print (datetime.datetime.today(),file=f)
f.close()
