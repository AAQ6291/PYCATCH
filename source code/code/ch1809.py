#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwin32com.client�Ҳ�
import win32com.client
import sys

# �إ�WMPlayer OCX����
app = win32com.client.Dispatch("SAPI.SpVoice")

print("�п�J��r, ��J�����UENTER, ���UCtrl+Z�����{��")
while True:
   try:
      # �N��J����r�ǵ�s�ܼ�
      s = raw_input()
      # �Ns�ܼƶǤJSpeck()��Ƥ�
      app.Speak(s)
   except:
      if sys.exc_type is EOFError:
         sys.exit()

