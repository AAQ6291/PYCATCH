#!/usr/bin/env python
#coding=cp950

import sys

if sys.platform == "win32":
   print("Windows�t��")
elif sys.platform == "mac":
   print("Mac�t��")
else:
   print("Posix/Linux/*BSD�Ψ�L�@�~�t��")
