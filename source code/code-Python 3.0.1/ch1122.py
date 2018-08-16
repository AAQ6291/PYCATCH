#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip

# 要壓縮的文字
text ="""
這裡是壓縮的文字內容...
""".encode('utf-8')

# 建立一個壓縮檔
f = gzip.open("./test.gz", "wb")

print("寫入:", text.decode('utf-8'))
# 將資料寫入壓縮檔
f.write(text)

# 關閉壓縮檔
f.close()

# 讀取壓縮內容
f = gzip.open("./test.gz", "rb")

# 讀取壓縮檔內容
content = f.read()
# 關閉壓縮檔
f.close()

# 輸出壓縮檔內容
print("解壓縮:", content.decode('utf-8'))
