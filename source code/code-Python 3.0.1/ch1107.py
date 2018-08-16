#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

# 讀取原始jpg檔ch1102.jpg
f = open("ch1102.jpg", "rb")

# 在讀取檔案內容同時將內容轉換成base64
text = f.read().encode("base64")

# 關閉檔案
f.close()


# 將編碼後的檔案寫入ch1102_64.jpg
f = open("ch1102_64.jpg", "wb")
f.write(text)

# 關閉檔案
f.close()


# 讀取編碼後的檔案
filename = "ch1102_64.jpg"
f = open(filename, "rb")

# 在讀取的過程中同時進行base64解碼
text = f.read().decode("base64")

# 關閉檔案
f.close()


# 將讀取並解碼後的base64內容寫入新的檔案_ch1102_64.jpg
f = open("_ch1102_64.jpg", "wb")
f.write(text)

# 關閉檔案
f.close()


