#!/usr/bin/env python
#coding=cp950

# ���Jtime�Ҳ�
import time

now = time.localtime(time.time())
print("��a�ɶ�:")
print(now)

print
now = time.localtime(time.time())[:6]
print("��a�ɶ�:")
print(now)

print
now = time.gmtime(time.time())
print("UTC�ɶ�:")
print(now)

print
now = time.gmtime(time.time())[:6]
print("UTC�ɶ�:")
print(now)
