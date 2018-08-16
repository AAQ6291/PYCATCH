#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入執行緒模組
import threading

# 定義類別並繼承threading.Thread類別
class myThread(threading.Thread):
   def __init__(self, threadID):
      
      # 定義 overriding threading.Thread.__init__
      threading.Thread.__init__(self)
      
      self.threadID = threadID

   # 定義run函數, 當使用start()函數後將會執行這個函數.
   def run(self):
      for i in range(10):
         print("[threadID = %d] >> %d \n" % (self.threadID, i))

if __name__=="__main__":
   # 建立5個執行緒物件
   for x in range(5):
      thread = myThread(x)
      thread.start()
      #thread.join()

   
   

