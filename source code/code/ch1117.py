#!/usr/bin/env python
# -*- coding: utf-8 -*-

import filecmp

print "比較 ch101.py 與 ch101.py是否相等", filecmp.cmp("./ch101.py", "./ch101.py")

print "比較 ch101.py 與 ch102.py是否相等", filecmp.cmp("./ch101.py", "./ch102.py")
