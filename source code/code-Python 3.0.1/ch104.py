#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

def gcd(x,y):
   while y:
      x, y = y, x % y
   return x

result = gcd(48,60)
print ("最大公因數=",result,sep="")
