#!/usr/bin/env python
#coding=cp950

# ���Jtime�Ҳ�
import time

# �w�qtime1���ի��A
time1 = (2008, 12, 30, 11, 20, 21, 0, 56, 1)
# ��ܥثe����
print "time1 = ", time1
# ��ܥثe�����A
print "���A = ", type(time1)
print

# �Ntime1�ഫ���ɶ�
time1 = time.mktime(time1)
# ��X�ഫ�᪺���G
print "time1 = ", time1
# ��ܥثe�����A
print "���A = ", type(time1)
# �ǤJtime.localtime()���
print "time.localtime = ", time.localtime(time1)
print

# �ɶ��p��, time1�Ptime2�t�F�@��
time1 = (2008, 12, 29, 11, 20, 21, 0, 56, 1)
time2 = (2008, 12, 30, 11, 20, 21, 0, 56, 1)

# �ϥ�time.mktime()��ƱNtime1�Ptime2���ի��A�ഫ���ɶ��íp��^�Ǭ��
print "time2 - time1"
second = time.mktime(time2) - time.mktime(time1)
print "time2 - time1 = ", second, "��"

# �p��t�X��
print "time2 - time1 = ", second / 60, "��"

# �p��t�X�Ӥp��
print "time2 - time1 = ", second / (60*60), "�p��"

# �p��t�X��
print "time2 - time1 = ", second / (60*60*24), "��"

