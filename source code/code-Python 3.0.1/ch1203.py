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

# 傳送資料
s.send('hi, how are you?'.encode('utf-8'))

# 接收從伺服端傳來的資料
data = s.recv(1024)

# 關閉連線
s.close()

print("收到訊息:")
print(repr(data))
