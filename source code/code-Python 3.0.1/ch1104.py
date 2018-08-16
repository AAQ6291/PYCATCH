#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

# 這裡是要進行編碼的文字內容
text = """
每天都有可以用 Google 做的事， 你可以用 Google 做什麼？發現更多。
""".encode('utf-8')

# 對字串進行編碼, 並將結果傳遞給en變數
en = base64.encodestring(text)

print("base64 編碼後的結果：\n %s" % (en))

# 將編碼後的結果進行解碼
de = base64.decodestring(en)

print("base64 解碼後的結果：\n %s" % (de.decode('utf-8')))
