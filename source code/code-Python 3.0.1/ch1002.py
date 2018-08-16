#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入執行緒模組
import _thread

# 建立fun()函數
def fun(threadID, x):
   for i in range(x):
      print("[threadID = %d] >> %d \n" % (threadID, i))

def myThread():
   # 建立5個執行緒同時執行fun()函數
   for x in range(5):
      _thread.start_new_thread(fun, (x, 10))

myThread()
