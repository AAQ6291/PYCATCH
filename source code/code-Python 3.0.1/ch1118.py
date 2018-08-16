#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入fileinput與sys模組
import fileinput, sys

# 使用fileinput.input()函數開啟檔案
f = fileinput.input("./ch101.py")
i = 1
# 輸出
for x in f:
   sys.stdout.write("%d>> " % (i))
   sys.stdout.write(x)
   i += 1

f.close()
