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

# �����Ȥ�ݰe�Ӫ����, �p�G�S���N���}while
while True:
   data = client.recv(1024)
   if not data:
      break

   # �^�Ǹ�Ƶ��Ȥ��
   client.send(data)
s.close()
