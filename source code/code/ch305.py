#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

import random

x = raw_input("請輸入一個數字:")
number = random.randint(0,10)

if int(x) >= number:
   print("輸入的文字大於或等於", number)
else:
   print("輸入的文字小於或等於", number)   
   
