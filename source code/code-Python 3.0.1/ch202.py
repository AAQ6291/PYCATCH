#!/usr/bin/env python
#coding=utf-8
from __future__ import print_function

x = None

## if not條件式，是說如果x變數為空值型態時就成立。
if not x:
   print("結果：條件式成立")
else:
   print("結果：條件式不成立")

x = ""

## 接著將x變數設為空字串，看if not條件式會不會成立。
if not x:
   print("結果：條件式成立")
else:
   print("結果：條件式不成立")

## 注意，x是不等於y，空字串與空格字串是不相同意思的。
y = " "
print("result:", x!=y)
