#!/usr/bin/env python
#coding=cp950

# 載入tarfile模組
import tarfile

"""
建立ch1146.tar.gz壓縮檔, mode引數使用"a".
mode = a 表示當ch1146.tar.gz不存在時會自動建立
"""
tar = tarfile.open("./ch1146.tar.gz", mode = "a")

# 將ch101.py, ch102.py與ch103.py檔案加入壓縮檔內.
for name in ["ch101.py","ch102.py","ch103.py"]:
   #加入
   tar.add(name)

# 關閉壓縮檔
tar.close()
