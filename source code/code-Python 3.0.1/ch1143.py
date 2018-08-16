#!/usr/bin/env python
#coding=cp950

import sys

if sys.platform == "win32":
   print("Windows系統")
elif sys.platform == "mac":
   print("Mac系統")
else:
   print("Posix/Linux/*BSD或其他作業系統")
