#!/usr/bin/env python
#coding=cp950

# 載入tarfile模組
import tarfile

# 讀取壓縮檔
tar = tarfile.open("./ch1146.tar.gz")

#解壓縮到ch1146資料夾, extractall 會自動建立資料夾.
tar.extractall("./ch1146")

# 關閉壓縮檔
tar.close()
