#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

while 1:
   text = raw_input("輸入任何字母:")
   if text == '\\q':
      break

   if len(text) < 5:
      continue

   print("您輸入的字母長度大於5")



