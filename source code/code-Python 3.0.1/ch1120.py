#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入ftplib模組
import ftplib

# 建立FTP連線與FTP instance
ftp = ftplib.FTP("192.168.1.1")

# 使用帳號與密碼登入
print(ftp.login("user","passwd"))

# 取得歡迎訊息
print(ftp.getwelcome())

# 列出目前的檔案與目錄列表
ftp.retrlines("LIST")

# 切換目錄到 upload
ftp.cwd("upload")

# 上傳ch205.txt檔案
ftp.storlines("STOR ch205.txt", open("./ch205.txt"))
"""
上傳成功的訊息如下：
'226-File successfully transferred\n226 0.390 seconds (measured here), 1.20 Kbytes per second'
"""

# 列出目前的檔案與目錄列表
ftp.dir()

# 結束FTP
print(ftp.quit())
