#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in x:
   ## 如果變數i的值無法被2整除的數字就略過。
   if i % 2 != 0:
      continue
      ## 在continue之後的程式碼都不會被執行。
      print("這行不會被執行到")
   else:
      ## 當i變數的值可以被2整除就印出。
      print(i)


