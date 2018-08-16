#!/usr/bin/env python
#coding=cp950

import sys

print("程式名稱與路徑: %s" % (sys.argv[0]))

if len(sys.argv) > 1:
   print("輸入的參數如下: \n")
   for arg in sys.argv[1:]:
      print(arg)
else:
   print("沒有任何參數")
   
