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

# �ϥΤG�i��Ҧ��}�ҭn�ǿ骺�ɮ�
f = open("c:\\python-2.6.msi", "rb")

# �N���e������ǻ���data�ܼ�
data = f.read()

# �����ɮ�
f.close()

# �ǰe�ɮ�
s.send(data)

# �����s�u
s.close()

