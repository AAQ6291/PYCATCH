#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���J������Ҳ�
import _thread
import time

# �إ�fun()���
def fun(threadID, x, lock):
   for i in range(x):
      # ���
      lock.acquire()
      time.sleep(1)
      print("[threadID = %d] >> %d \n" % (threadID, i))
      # ����
      lock.release()
      time.sleep(1)

def myThread():
   # �إ�5�Ӱ�����P�ɰ���fun()���
   lock = _thread.allocate_lock()
   for x in range(5):
      _thread.start_new_thread(fun, (x, 10, lock))

myThread()
