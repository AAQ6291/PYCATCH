#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���J_winreg�Ҳ�
import _winreg

# �}�Ҥ@��Key �ó]�w _winreg.KEY_ALL_ACCESS �Ѽ�.
reg = _winreg.OpenKey(
   _winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python",
   0,
   _winreg.KEY_ALL_ACCESS)

print "�}�� Software\\Microsoft\\Internet Explorer\\Main\\Python"

# �R�����U���
_winreg.DeleteValue(
   reg,
   "NewOne")

print "�R�� name=NewOne, type=REG_SZ, value='123'"

# �R���n����key��
_winreg.DeleteKey(
   _winreg.HKEY_LOCAL_MACHINE,
   "Software\\Microsoft\\Internet Explorer\\Main\\Python")

print "�R�� Software\\Microsoft\\Internet Explorer\\Main\\Python"

