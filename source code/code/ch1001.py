#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���J������Ҳ�
import thread

# �إ�fun()���
def fun(x):
   print('thread >> %d \n' % x)

def myThread():
   # �إ�5�Ӱ�����P�ɰ���fun()���
   for x in range(5):
      thread.start_new_thread(fun, (x,))

myThread()
