#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入執行緒模組
import _thread
import time

# 建立fun()函數
def fun(threadID, x, lock):
   for i in range(x):
      # 鎖住
      lock.acquire()
      time.sleep(1)
      print("[threadID = %d] >> %d \n" % (threadID, i))
      # 解鎖
      lock.release()
      time.sleep(1)

def myThread():
   # 建立5個執行緒同時執行fun()函數
   lock = _thread.allocate_lock()
   for x in range(5):
      _thread.start_new_thread(fun, (x, 10, lock))

myThread()
