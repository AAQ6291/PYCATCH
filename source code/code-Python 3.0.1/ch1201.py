#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jsocket�Ҳ�
import socket

# �إ�socket����
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# �M��s�u���ݤf
port = socket.getservbyname('http', 'tcp')

# �إ߳s�u
s.connect(('www.google.com',port))
print(s)

print("�^�Ǧۤv��IP�P�q�T�ݤf:")
print(s.getsockname())

print("�^�ǻ��ݪ�IP�P�s�u�ݤf:")
print(s.getpeername())

# �����s�u
s.close()
