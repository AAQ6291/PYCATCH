#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function
import random

## 宣告x序列變數
x = ['a','b','c','d','e']

## 使用for敘述句逐筆印出。
for x1 in x:
   ##但是如果不小心在敘述區塊裡改變了x的長度，將會出現不可預期的問題。
   x.append(x1)
   print(x1)

   ## Windows 使用者請按 Ctrl + C 進行中斷此程式
   ## Linux 使用者請按 Ctrl + Z  進行中斷此程式
   
