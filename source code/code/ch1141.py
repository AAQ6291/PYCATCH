#!/usr/bin/env python
#coding=cp950

import sys

find_module = "wx"

if find_module in sys.builtin_module_names:
   print("%s�O���m�Ҳ�." % (find_module))
else:
   print(__import__(find_module))
   
