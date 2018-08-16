#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

text = """
每天都有可以用 Google 做的事， 你可以用 Google 做什麼？發現更多。
""".encode('utf-8')
filename = "data.dat"
filename_en = "64data.dat"

# 先將要編碼的文字寫入data.dat檔案
f = open(filename, "wb")
f.write(text)
# 記得要關閉檔案
f.close()

# 開啟檔案進行編碼
base64.encode(open(filename, "rb"), open(filename_en, "wb"))

# 開啟檔案進行解碼
base64.decode(open(filename_en, "rb"), open(filename, "wb"))

# 輸出到畫面
print("編碼後的內容: \n %s " % open(filename_en, "rb").read())
print("解碼後的內容: \n %s " % open(filename, "rb").read().decode('utf-8'))
