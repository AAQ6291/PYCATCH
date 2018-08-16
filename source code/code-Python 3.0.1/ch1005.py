#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jtime, threading�PQueue�Ҳ�
import time
import threading
import queue

# �w�qPutQueue���O
class PutQueue(threading.Thread):
   """
   �w�qPutQueue���O, �o�����O�O�N�u�@��J��C�̵���Worker���O�B�z��C�����u�@.
   """
   def __init__(self,count,itemq):
      threading.Thread.__init__(self)
      self.itemq=itemq
      self.count = count

   """
   �o��run method(��k)�O�и�Thread.run(),
   self.itemq.put()�N�OQueue.put()���, �ηN�O�N�u�@��J��C.
   """
   def run(self):
      print("�����%s >> �N�u�@�s�� %d ��J��C: \n" % (threading.currentThread(), self.count))
      self.itemq.put(self.count)
      time.sleep(1)

# �w�qWorker���O
class Worker(threading.Thread):
   """
   �o�����O�O�b�B�z��C�����u�@
   """
   def __init__(self,itemq):
      threading.Thread.__init__(self)
      self.itemq = itemq

   """
   �o��run method(��k)�O�и�Thread.run(),
   self.itemq.get()�N�OQueue.get()���, �ηN�O�B�z��C�����u�@.
   �B�z���u�@�ᥲ���ŧiself.itemq.task_done()
   self.itemq.task_done()�N�OQueue.task_done(), �ηN�O�i�D��C�Ӥu�@���ؤw����
   """
   def run(self):
      while True:
         try:
            current = self.itemq.get()
            print("�����%s >> �B�z�u�@�s�� %d: \n" % (threading.currentThread(), current))
            self.itemq.task_done()
            time.sleep(2)
         except queue.Empty:
            print("��C�Ū�")
            break

       
if __name__=="__main__":

   """
   �@��b�ŧiQueue.Queue()�i�H���ε���, �b�����Ȫ����p�U��ܤ�����Queue���j�p,
   ���d�ҬO�]�wQueue���e�q��10, ��̦ܳh�u���10�Ӥu�@�b��C��,
   �p�G��C���F�N���������ӱ��@�Ǥu�@��~��A��s���u�@���C�̡C
   """
   queue = queue.Queue(10)
   for x in range(10):
      pq=PutQueue(x,queue)
      pq.start()
      pq.join()

   """
   �o�̫ŧi�F��Ӱ�����ӳB�z��C�����u�@
   """
   for x in range(2):
      worker1 = Worker(queue)
      worker2 = Worker(queue)
      worker1.start()
      worker2.start()

   queue.join()
    
    
