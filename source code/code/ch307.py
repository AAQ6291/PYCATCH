#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

import random

x = random.randint(1,100)

while (1):
   number = int(raw_input("猜數字，輸入一個數字:"))
   if x == number:
      print("您猜對了!")
      break
   elif x > number:
      print("比",number,"大")
   elif x < number:
      print("比",number,"小")
   
   
