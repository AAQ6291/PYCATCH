#!/usr/bin/env python
#coding=cp950

# ���Jtarfile�Ҳ�
import tarfile

# Ū�����Y��
tar = tarfile.open("./ch1146.tar.gz")

# �C�X���Y�ɪ����e
print("�ɮ�:\t\t\t�j�p:")
print("-" * 30)
for file in tar.getmembers():
   print("%s\t\t\t%s" % (file.name, file.size))

# �������Y��
tar.close()
