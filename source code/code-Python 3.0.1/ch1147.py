#!/usr/bin/env python
#coding=cp950

# ���Jtarfile�Ҳ�
import tarfile

# Ū�����Y��
tar = tarfile.open("./ch1146.tar.gz")

#�����Y��ch1146��Ƨ�, extractall �|�۰ʫإ߸�Ƨ�.
tar.extractall("./ch1146")

# �������Y��
tar.close()
