#!C:\Python26\python
# -*- coding: cp950 -*-

def myFunction(name):
   "函數說明..."
   return "(這是呼叫Python語言裡的函數) , 您好 %s!\n" % (name)

name = raw_input("輸入姓名:")
if name:
   print(myFunction(name))
