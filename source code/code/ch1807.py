#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwin32com.client�Ҳ�
import win32com.client
import time

# �إ�IE����
app = win32com.client.Dispatch("InternetExplorer.Application")

# ���IE�s����
app.Visible = 0

# �}�Һ���
app.Navigate("http://www.google.com.tw")

# ���ݺ����}��
while app.ReadyState != 4:
   time.sleep(2)

# �u�����o�������e����r
text = app.Document.body.innerText
# Unicode�ഫ
text = unicode(text)

# �����{��
app.Quit()

#��X������G
print(text)
