#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���J������Ҳ�
import thread

# �إ�fun()���
def fun(threadID, x):
   for i in range(x):
      print("[threadID = %d] >> %d \n" % (threadID, i))

def myThread():
   # �إ�5�Ӱ�����P�ɰ���fun()���
   for x in range(5):
      thread.start_new_thread(fun, (x, 10))

myThread()
