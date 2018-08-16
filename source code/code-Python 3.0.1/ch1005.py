#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入time, threading與Queue模組
import time
import threading
import queue

# 定義PutQueue類別
class PutQueue(threading.Thread):
   """
   定義PutQueue類別, 這個類別是將工作丟入佇列裡等待Worker類別處理佇列內的工作.
   """
   def __init__(self,count,itemq):
      threading.Thread.__init__(self)
      self.itemq=itemq
      self.count = count

   """
   這個run method(方法)是覆載Thread.run(),
   self.itemq.put()就是Queue.put()函數, 用意是將工作丟入佇列.
   """
   def run(self):
      print("執行緒%s >> 將工作編號 %d 放入佇列: \n" % (threading.currentThread(), self.count))
      self.itemq.put(self.count)
      time.sleep(1)

# 定義Worker類別
class Worker(threading.Thread):
   """
   這個類別是在處理佇列類的工作
   """
   def __init__(self,itemq):
      threading.Thread.__init__(self)
      self.itemq = itemq

   """
   這個run method(方法)是覆載Thread.run(),
   self.itemq.get()就是Queue.get()函數, 用意是處理佇列類的工作.
   處理完工作後必須宣告self.itemq.task_done()
   self.itemq.task_done()就是Queue.task_done(), 用意是告訴佇列該工作項目已完成
   """
   def run(self):
      while True:
         try:
            current = self.itemq.get()
            print("執行緒%s >> 處理工作編號 %d: \n" % (threading.currentThread(), current))
            self.itemq.task_done()
            time.sleep(2)
         except queue.Empty:
            print("佇列空的")
            break

       
if __name__=="__main__":

   """
   一般在宣告Queue.Queue()可以不用給值, 在不給值的情況下表示不限制Queue的大小,
   本範例是設定Queue的容量為10, 表示最多只能放10個工作在佇列裡,
   如果佇列滿了就必須先消耗掉一些工作後才能再放新的工作到佇列裡。
   """
   queue = queue.Queue(10)
   for x in range(10):
      pq=PutQueue(x,queue)
      pq.start()
      pq.join()

   """
   這裡宣告了兩個執行緒來處理佇列內的工作
   """
   for x in range(2):
      worker1 = Worker(queue)
      worker2 = Worker(queue)
      worker1.start()
      worker2.start()

   queue.join()
    
    
