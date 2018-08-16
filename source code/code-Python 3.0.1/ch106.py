#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

# 這是程式註解。
## 這也是程式註解。

# 如果您需要逐行註解的情況下，建議註解在每行的上面
print("這行後面的註解會被直譯器略過=>>") # 這行會被略過，但是一般並不建議這麼做。


''' 連續3個單引號程式註解
這是程式註解區塊，在這註解區塊內的程式碼會被略過。
x = 1
if x == 1:
   print("x == 1", x == 1)
'''

""" 連續3個雙引號程式註解
這是程式註解區塊，在這註解區塊內的程式碼會被略過。
x = 1
if x == 1:
   print("x == 1", x == 1)
"""