#!/usr/bin/env python
#coding=cp950

# ���Jtime�Ҳ�
import time

# �]�w�}�l�ɶ�
start_time = time.time()

# ����2��
time.sleep(3)

# �]�w�����ɶ�
end_time = time.time()

# �����ɶ� - �}�l�ɶ� = ����ɶ�
print("����ɶ�: %s ��" % (end_time - start_time))
