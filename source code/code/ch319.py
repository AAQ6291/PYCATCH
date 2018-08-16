#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function
import random

def apple():
   print("您選擇了蘋果")

def orange():
   print("您選擇了橘子")

def banana():
   print("您選擇了香蕉")

def default():
   print("沒有您選擇的")

case = "apple"

switch = {
   'apple' : apple,
   'orange' : orange,
   'banana' : banana,
}

switch.get(case, default)()
switch.get("coffee", default)()


