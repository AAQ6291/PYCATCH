#!/usr/bin/env python
#coding=cp950

# 載入tarfile模組
import tarfile

# 讀取壓縮檔
tar = tarfile.open("./ch1146.tar.gz")

# 列出壓縮檔的內容
print("檔案:\t\t\t大小:")
print("-" * 30)
for file in tar.getmembers():
   print("%s\t\t\t%s" % (file.name, file.size))

# 關閉壓縮檔
tar.close()
