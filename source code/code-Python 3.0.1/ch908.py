#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwinreg�Ҳ�
import winreg

# �إ�Ū���n���ɦ�m
reg = winreg.OpenKey(
   winreg.HKEY_LOCAL_MACHINE,
"Software\\Microsoft\\Internet Explorer\\Main")

"""
winreg.EnumValue()�|�^�Ǥ@��tuple�ȡA���Q��(�W��, ���, ����)
"""

# �ϥ�try...except�Pwhile True�v��Ū�X�n����
try:
   index = 0
   while True:
      # name = �W��, value = ���, type = ����
      name, value, type = winreg.EnumValue(reg, index)
      print(name, type, repr(value))
      index += 1
except:
   pass



