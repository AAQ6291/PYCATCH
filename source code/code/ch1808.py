#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwin32com.client�Ҳ�
import win32com.client

# �إ�WMPlayer OCX����
app = win32com.client.Dispatch("WMPlayer.OCX")

# Ū��������
play_file = app.openPlayer("c:\\song44.mp3")

# �إ߱��
control = app.controls

# ����
control.play()

