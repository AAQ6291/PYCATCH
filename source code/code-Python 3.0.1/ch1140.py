#!/usr/bin/env python
#coding=cp950

import sys

print("�{���W�ٻP���|: %s" % (sys.argv[0]))

if len(sys.argv) > 1:
   print("��J���ѼƦp�U: \n")
   for arg in sys.argv[1:]:
      print(arg)
else:
   print("�S������Ѽ�")
   
