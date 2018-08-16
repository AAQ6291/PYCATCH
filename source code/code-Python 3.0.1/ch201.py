#!/usr/bin/env python
#coding=utf-8
from __future__ import print_function

## 步驟1.宣告x=1.0，因為x並不是空值，所以不會進入if條件式print()結果。
x = 1.0
if x == None:
   print("1. x = ",x)

## 步驟2.宣告了x=None，所以if條件式成立後進入print()結果。
x = None
if x == None:
   print("2. x = ",x, type(x))

## 步驟3.宣告了x=""，這是空字串，並不是空值型態(None Type)，所以if條件式不成立。
x = ""
if x == None:
   print("3. x = ",x)

## 步驟4.將if條件式改為判斷空字串，條件成立，所以會print()出結果。
x = ""
if x == "":
   print("4. x = ",x, type(x))
