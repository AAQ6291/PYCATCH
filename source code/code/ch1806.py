#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwin32com.client�Ҳ�
import win32com.client
import time

# �إ�IE����
app = win32com.client.Dispatch("InternetExplorer.Application")

# ���IE�s����
app.Visible = 1

app.Navigate("http://www.google.com")

# ���ݺ����}��
while app.ReadyState != 4:
   time.sleep(2)

# ���o���������s��URL
try:   
   for link in app.Document.links:
      print link
except:
   pass
