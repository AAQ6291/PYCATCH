#!/usr/bin/env python
#coding=cp950

# ���Jtarfile�Ҳ�
import tarfile

"""
�إ�ch1146.tar.gz���Y��, mode�޼ƨϥ�"a".
mode = a ��ܷ�ch1146.tar.gz���s�b�ɷ|�۰ʫإ�
"""
tar = tarfile.open("./ch1146.tar.gz", mode = "a")

# �Nch101.py, ch102.py�Pch103.py�ɮץ[�J���Y�ɤ�.
for name in ["ch101.py","ch102.py","ch103.py"]:
   #�[�J
   tar.add(name)

# �������Y��
tar.close()
