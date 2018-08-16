#!/usr/bin/env python
#coding=cp950

# 載入tempfile模組
import tempfile

# 建立暫存檔案
tf = tempfile.mktemp()
print("建立的暫存檔案位置:%s" % (tf))

# 寫入資料到暫存檔案
f = open(tf, "w")

# 將寫入內容
for line in range(10):
   f.writelines("test %s" % (line))

# 關閉
f.close()

# 開啟暫存檔案
f = open(tf, "r")

# 讀取內容
for line in f.readlines():
   print(line)

