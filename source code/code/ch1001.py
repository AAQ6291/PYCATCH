#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入執行緒模組
import thread

# 建立fun()函數
def fun(x):
   print('thread >> %d \n' % x)

def myThread():
   # 建立5個執行緒同時執行fun()函數
   for x in range(5):
      thread.start_new_thread(fun, (x,))

myThread()
