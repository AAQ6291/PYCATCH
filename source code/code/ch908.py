#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���J_winreg�Ҳ�
import _winreg

# �إ�Ū���n���ɦ�m
reg = _winreg.OpenKey(
   _winreg.HKEY_LOCAL_MACHINE,
"Software\\Microsoft\\Internet Explorer\\Main")

"""
_winreg.EnumValue()�|�^�Ǥ@��tuple�ȡA���Q��(�W��, ���, ����)
"""

# �ϥ�try...except�Pwhile True�v��Ū�X�n����
try:
   index = 0
   while True:
      # name = �W��, value = ���, type = ����
      name, value, type = _winreg.EnumValue(reg, index)
      print name, type, repr(value)
      index += 1
except:
   pass



