#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jsocket�Ҳ�
import socket

# �]�w�D����IP, �]���o�O���A�ݵ{���ҥH���γ]�wIP
server = ''

# �]�w�n�إߪ�port
port = 12000

# �إ�socket����
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# �ϥ�bind()��Ƹj��IP�PPORT��m�C
s.bind((server, port))

# listen()��ƬO�]�w�̤j���Ȥ�ݳs�u��
s.listen(1)

# �����s�u
client, addr = s.accept()

print('�s�uIP:')
print(addr)

# �N�������ɮר��s���W��, �H�G�i��Ҧ��g�J
f = open("c:\\python-2.6-TEST.msi", "wb")
while True:
   # �N��������ƶǻ���data�ܼ�
   data = client.recv(4096)
   
   # �Ndata�ܼƼg�J�ɮ�
   f.write(data)
   
   if not data:
      break

# �����s�u
s.close()
