#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入winreg模組
import winreg

# 建立讀取登錄檔位置
reg = winreg.OpenKey(
   winreg.HKEY_LOCAL_MACHINE,
"Software\\Microsoft\\Internet Explorer\\Main")

"""
winreg.EnumValue()會回傳一個tuple值，順利為(名稱, 資料, 類型)
"""

# 使用try...except與while True逐筆讀出登錄檔
try:
   index = 0
   while True:
      # name = 名稱, value = 資料, type = 類型
      name, value, type = winreg.EnumValue(reg, index)
      print(name, type, repr(value))
      index += 1
except:
   pass



