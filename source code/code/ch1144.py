#!/usr/bin/env python
#coding=cp950

# ���Jsys�Pstring�Ҳ�
import sys, string

# �w�qreOut���O
class reOut:
   def __init__(self, stdout):
      self.stdout = stdout

   # �и�write()���
   def write(self, str):
      # �N�r���ഫ���p�g
      self.stdout.write(string.lower(str))
      
# ���s�w�qsys.stdout
sys.stdout = reOut(sys.stdout)

# ��X���j�g�r���Q�אּ�p�g
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
