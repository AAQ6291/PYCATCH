#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入win32com.client模組
import win32com.client

# 建立WMPlayer OCX物件
app = win32com.client.Dispatch("WMPlayer.OCX")

# 讀取音樂檔
play_file = app.openPlayer("c:\\song44.mp3")

# 建立控制項
control = app.controls

# 播放
control.play()

