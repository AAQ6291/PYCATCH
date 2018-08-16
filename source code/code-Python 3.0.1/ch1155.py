#!/usr/bin/env python
#coding=cp950

# 載入timeit模組
import timeit

# 定義函數
def fun1():
   return True
   
if __name__ == "__main__":

   # 定義Timer並執行載入fun1後執行
   t = timeit.Timer("fun1()", "from __main__ import fun1")

   # 設定執行時間
   print(t.timeit(1000000))

   # 重覆執行fun1函數3次與執行時間
   print(t.repeat(3, 2000000))
