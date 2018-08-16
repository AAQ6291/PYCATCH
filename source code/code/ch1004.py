#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���J������Ҳ�
import threading

# �w�q���O���~��threading.Thread���O
class myThread(threading.Thread):
   def __init__(self, threadID):
      
      # �w�q overriding threading.Thread.__init__
      threading.Thread.__init__(self)
      
      self.threadID = threadID

   # �w�qrun���, ��ϥ�start()��ƫ�N�|����o�Ө��.
   def run(self):
      for i in range(10):
         print("[threadID = %d] >> %d \n" % (self.threadID, i))

if __name__=="__main__":
   # �إ�5�Ӱ��������
   for x in range(5):
      thread = myThread(x)
      thread.start()
      #thread.join()

   
   

