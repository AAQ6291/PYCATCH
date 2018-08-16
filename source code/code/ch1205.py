#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入socket模組
import socket

server = '127.0.0.1'
port = 12000
# 建立socket物件
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立連線
s.connect((server, port))

# 使用二進位模式開啟要傳輸的檔案
f = open("c:\\python-2.6.msi", "rb")

# 將內容€全部傳遞到data變數
data = f.read()

# 關閉檔案
f.close()

# 傳送檔案
s.send(data)

# 關閉連線
s.close()

