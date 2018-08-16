#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入win32com.client模組
import win32com.client
import sys

# 建立WMPlayer OCX物件
app = win32com.client.Dispatch("SAPI.SpVoice")

print("請輸入單字, 輸入完按下ENTER, 按下Ctrl+Z結束程式")
while True:
   try:
      # 將輸入的單字傳給s變數
      s = raw_input()
      # 將s變數傳入Speck()函數內
      app.Speak(s)
   except:
      if sys.exc_type is EOFError:
         sys.exit()

