#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

char1 = raw_input("請輸入鍵盤上隨意一個英文字母:")
char2 = raw_input("請輸入鍵盤上隨意一個英文字母:")

if char1 < char2:
   print(">>", char1, "比", char2, "小", sep="")

if char1 > char2:
   print(">>", char1, "比", char2, "大", sep="")

if char1 == char2:
   print(">>", char1, "與", char2, "相等", sep="")
