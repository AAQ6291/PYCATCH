#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bz2

text = """
Python在近年來已經成為現今成長速度最快的程式語言...
"""

# 將文字壓縮到ch1110.bz2壓縮檔
f = bz2.BZ2File("./ch1110.bz2", "w")
f.write(text)
f.close()

# 讀取ch1110.bz2壓縮檔的內容
f = bz2.BZ2File("./ch1110.bz2", "r")
for x in f:
   print x
f.close()
   
