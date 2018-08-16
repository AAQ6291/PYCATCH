#!/usr/bin/env python
#coding=cp950

import sys

# 使用sys.modules.keys()取得目前有載入(import)的模組名稱
for x in sys.modules.keys():
   print(x)
