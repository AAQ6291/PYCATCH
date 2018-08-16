#!C:\Python26\python
# -*- coding: cp950 -*-

import fib

n = raw_input("輸出要計算費氏數列前幾項:")
if n:
   print(fib.fib(int(n)))

# 輸出函數說明
print ("fib.fib.__doc__ = %s" % (fib.fib.__doc__))
