#!/usr/bin/env python
#coding=cp950

# 載入sys模組
import sys

# 定義reOut類別
class reOut:
   def __init__(self, stdout):
      self.stdout = stdout

   # 覆載write()函數
   def write(self, str):
      # 將字母轉換為小寫
      self.stdout.write(str.lower())
      
# 重新定義sys.stdout
sys.stdout = reOut(sys.stdout)

# 輸出的大寫字母被改為小寫
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
