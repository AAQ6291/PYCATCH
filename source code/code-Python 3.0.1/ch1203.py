#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jsocket�Ҳ�
import socket

server = '127.0.0.1'
port = 12000
# �إ�socket����
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# �إ߳s�u
s.connect((server, port))

# �ǰe���
s.send('hi, how are you?'.encode('utf-8'))

# �����q���A�ݶǨӪ����
data = s.recv(1024)

# �����s�u
s.close()

print("����T��:")
print(repr(data))
