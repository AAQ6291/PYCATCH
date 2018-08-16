#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入_winreg模組
import _winreg

# 建立一個Key
reg = _winreg.CreateKey(
   _winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python")

print "建立完成", "Software\\Microsoft\\Internet Explorer\\Main\\Python"

# 寫入註冊資料
_winreg.SetValueEx(
   reg,
   "NewOne",
   0,
   _winreg.REG_SZ,
   "123")

print "建立完成 name=NewOne, type=REG_SZ, value='123'"

# 寫入註冊資料
_winreg.SetValueEx(
   reg,
   "NewTwo",
   0,
   _winreg.REG_BINARY,
   "1")

print "建立完成 name=NewTwo, type=REG_BINARY, value='1'"
