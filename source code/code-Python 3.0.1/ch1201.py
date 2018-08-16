#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入socket模組
import socket

# 建立socket物件
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 尋找連線的端口
port = socket.getservbyname('http', 'tcp')

# 建立連線
s.connect(('www.google.com',port))
print(s)

print("回傳自己的IP與通訊端口:")
print(s.getsockname())

print("回傳遠端的IP與連線端口:")
print(s.getpeername())

# 關閉連線
s.close()
