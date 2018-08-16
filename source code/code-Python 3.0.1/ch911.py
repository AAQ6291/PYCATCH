#!/usr/bin/env python
# -*- coding: cp950 -*-

# 開啟檔案
f = open("./sample.txt", "r+")

# 讀取
for line in f:
   print(line)

# 關閉
f.close()
