#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���J������Ҳ�
import _thread

# �إ�fun()���
def fun(threadID, x):
   for i in range(x):
      print("[threadID = %d] >> %d \n" % (threadID, i))

def myThread():
   # �إ�5�Ӱ�����P�ɰ���fun()���
   for x in range(5):
      _thread.start_new_thread(fun, (x, 10))

myThread()
