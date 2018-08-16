#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function
import random

def do():
   """
   定義一個do()函數，函數內會依序印出x的x次方，
   最後return False
   """
   for x in range(1, 10):
      print("x**x =", x**x, sep="")
   return False

## 宣告使用while無限迴圈。
while True:
   
   ## 呼叫do()函數
   x = do()
   
   ## 如果x為False就跳離while
   if not x:
      break

## 最後印出結果
print("End of do-while.")
   
