#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入ftplib模組
import ftplib

# 建立FTP連線與FTP instance
ftp = ftplib.FTP("ftp.freebsd.org")

# 暱名登入（account:anonymous, password:email@...）
print ftp.login()

# 取得歡迎訊息
print ftp.getwelcome()

# 列出目前的檔案與目錄列表
ftp.retrlines("LIST")

# 切換目錄到 pub/FreeBSD
ftp.cwd("pub/FreeBSD")

# 列出目前的檔案與目錄列表
ftp.dir()

# 下載README.TXT檔案並寫入到自己的電腦裡.
ftp.retrbinary('RETR README.TXT', open('README.TXT', 'wb').write)

# 結束FTP
print ftp.quit()
