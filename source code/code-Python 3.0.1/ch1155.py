#!/usr/bin/env python
#coding=cp950

# ���Jtimeit�Ҳ�
import timeit

# �w�q���
def fun1():
   return True
   
if __name__ == "__main__":

   # �w�qTimer�ð�����Jfun1�����
   t = timeit.Timer("fun1()", "from __main__ import fun1")

   # �]�w����ɶ�
   print(t.timeit(1000000))

   # ���а���fun1���3���P����ɶ�
   print(t.repeat(3, 2000000))
