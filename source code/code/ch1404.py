#!C:\Python26\python
# -*- coding: cp950 -*-

import my

name = raw_input("輸入姓名:")
if name:
   my.myFunction(name)

# 輸出函數說明
print my.myFunction.__doc__
