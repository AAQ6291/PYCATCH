#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function
import random

hand = ['剪刀','石頭','布']

while True:
   x = int(raw_input("請輸入數字 0)剪刀 1)石頭 2)布:"))
   rand = random.choice(hand)

   if x == 0 and hand.index(rand) == 1:
      print("輸了!電腦是", rand, sep="")
   if x == 1 and hand.index(rand) == 0:
      print("贏了!電腦是", rand, sep="")
      break

   if x == 1 and hand.index(rand) == 2:
      print("輸了!電腦是", rand, sep="")
   if x == 2 and hand.index(rand) == 1:
      print("贏了!電腦是", rand, sep="")
      break

   if x == 2 and hand.index(rand) == 0:
      print("輸了!電腦是", rand, sep="")
   if x == 0 and hand.index(rand) == 2:
      print("贏了!電腦是", rand, sep="")
      break

   if x == 0 and hand.index(rand) == 0:
      print("平手!電腦是", rand, sep="")
   if x == 1 and hand.index(rand) == 1:
      print("平手!電腦是", rand, sep="")
   if x == 2 and hand.index(rand) == 2:
      print("平手!電腦是", rand, sep="")
