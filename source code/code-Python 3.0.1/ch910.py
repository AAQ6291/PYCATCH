#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwinreg�Ҳ�
import winreg

# �}�Ҥ@��Key �ó]�w winreg.KEY_ALL_ACCESS �Ѽ�.
reg = winreg.OpenKey(
   winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python",
   0,
   winreg.KEY_ALL_ACCESS)

print("�}�� Software\\Microsoft\\Internet Explorer\\Main\\Python")

# �R�����U���
winreg.DeleteValue(
   reg,
   "NewOne")

print("�R�� name=NewOne, type=REG_SZ, value='123'")

# �R���n����key��
winreg.DeleteKey(
   winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python")

print("�R�� Software\\Microsoft\\Internet Explorer\\Main\\Python")

