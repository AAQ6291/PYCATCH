#!/usr/bin/env python
#coding=cp950

# ���Jtempfile�Ҳ�
import tempfile

# �إ߼Ȧs�ɮ�
tf = tempfile.mktemp()
print("�إߪ��Ȧs�ɮצ�m:%s" % (tf))

# �g�J��ƨ�Ȧs�ɮ�
f = open(tf, "w")

# �N�g�J���e
for line in range(10):
   f.writelines("test %s" % (line))

# ����
f.close()

# �}�ҼȦs�ɮ�
f = open(tf, "r")

# Ū�����e
for line in f.readlines():
   print(line)

