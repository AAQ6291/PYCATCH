#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���J_winreg�Ҳ�
import _winreg

# �إߤ@��Key
reg = _winreg.CreateKey(
   _winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python")

print "�إߧ���", "Software\\Microsoft\\Internet Explorer\\Main\\Python"

# �g�J���U���
_winreg.SetValueEx(
   reg,
   "NewOne",
   0,
   _winreg.REG_SZ,
   "123")

print "�إߧ��� name=NewOne, type=REG_SZ, value='123'"

# �g�J���U���
_winreg.SetValueEx(
   reg,
   "NewTwo",
   0,
   _winreg.REG_BINARY,
   "1")

print "�إߧ��� name=NewTwo, type=REG_BINARY, value='1'"
