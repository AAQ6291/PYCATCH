#!/usr/bin/env python
#coding=utf-8
from __future__ import print_function

## 宣告x, y, z變數，各分別為tuple, list, dict資料型態。
x, y, z = (), [], {}

## 雖然都是空的結構，但是它們之間並不相等。
if x == y == z:
   print(x, y, z, "相等")
else:
   print(x, y, z, "不相等")

if x == None:
   print(x, " 相等 None")
else:
   print(x, " 不相等 None")

if y == None:
   print(y, " 相等 None")
else:
   print(y, " 不相等 None")

if z == None:
   print(z, " 相等 None")
else:
   print(z, " 不相等 None")

