#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入_winreg模組
import _winreg

# 開啟一個Key 並設定 _winreg.KEY_ALL_ACCESS 參數.
reg = _winreg.OpenKey(
   _winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python",
   0,
   _winreg.KEY_ALL_ACCESS)

print "開啟 Software\\Microsoft\\Internet Explorer\\Main\\Python"

# 刪除註冊資料
_winreg.DeleteValue(
   reg,
   "NewOne")

print "刪除 name=NewOne, type=REG_SZ, value='123'"

# 刪除登錄檔key值
_winreg.DeleteKey(
   _winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python")

print "刪除 Software\\Microsoft\\Internet Explorer\\Main\\Python"

