#!/usr/bin/env python
#coding=cp950

# 更sys籔string家舱
import sys, string

# ﹚竡reOut摸
class reOut:
   def __init__(self, stdout):
      self.stdout = stdout

   # 滦更write()ㄧ计
   def write(self, str):
      # 盢ダ锣传糶
      self.stdout.write(string.lower(str))
      
# 穝﹚竡sys.stdout
sys.stdout = reOut(sys.stdout)

# 块糶ダ砆э糶
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
