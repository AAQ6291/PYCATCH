#!/usr/bin/env python
#coding=cp950

# ���Jtime�Ҳ�
import time

# �w�q�ɶ�
now = time.localtime(time.time())

# �N�ɶ��H�r��榡��X
print(time.asctime(now))

# �w�q�ɶ�
now = time.time()

# �N�ɶ��H�r��榡��X
print(time.ctime(now))
