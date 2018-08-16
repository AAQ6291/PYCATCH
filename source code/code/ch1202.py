#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入socket模組
import socket

# 設定主機的IP, 因為這是伺服端程式所以不用設定IP
server = ''

# 設定要建立的port
port = 12000

# 建立socket物件
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 使用bind()函數綁住此IP與PORT位置。
s.bind((server, port))

# listen()函數是設定最大的客戶端連線數
s.listen(1)

# 接受連線
client, addr = s.accept()

print('連線IP:')
print(addr)

# 接收客戶端送來的資料, 如果沒有就離開while
while True:
   data = client.recv(1024)
   if not data:
      break

   # 回傳資料給客戶端
   client.send(data)
s.close()
