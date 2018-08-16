#!/usr/bin/env python
#coding=utf-8
from __future__ import print_function

def credit(TotalPrice,num):
   ## 學分總費用除以幾個學分
   price = TotalPrice / num
   return price

print(credit(33300,9))
