#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwinreg�Ҳ�
import winreg

# �إߤ@��Key
reg = winreg.CreateKey(
   winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python")

print("�إߧ���", "Software\\Microsoft\\Internet Explorer\\Main\\Python")

# �g�J���U���
winreg.SetValueEx(
   reg,
   "NewOne",
   0,
   winreg.REG_SZ,
   "123")

print("�إߧ��� name=NewOne, type=REG_SZ, value='123'")

# �g�J���U���
winreg.SetValueEx(
   reg,
   "NewTwo",
   0,
   winreg.REG_BINARY,
   b'1')

print("�إߧ��� name=NewTwo, type=REG_BINARY, value='1'")
