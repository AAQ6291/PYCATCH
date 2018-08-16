#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入gzip模組
import gzip

# 開啟預計要新增到壓縮內的檔案
file_in = open("./ch205.txt", "rb")

"""
開啟原先已經存在的壓縮檔, 注意這裡的mode引數是使用ab,
ab是代表會先著原本的檔案寫入, 現在壓縮檔的內容為:

"這裡是壓縮的文字內容..."

使用ab模式寫入後的壓縮檔內容為:

"
這裡是壓縮的文字內容...
Python在近年來已經成為現今成長速度最快的程式語言，
...
"
"""
file_out = gzip.open("./test.gz", "ab")

# 將內容寫入壓縮檔
file_out.writelines(file_in)

# 關閉壓縮檔
file_out.close()

# 關閉檔案
file_in.close()


# 讀取壓縮內容
f = gzip.open("./test.gz", "rb")

# 讀取壓縮檔內容
content = f.read()
# 關閉壓縮檔
f.close()

# 輸出壓縮檔內容
print "解壓縮:", content
