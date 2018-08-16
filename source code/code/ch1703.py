#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入wx模組
import wx

# 建立myApp類別並繼承wx.App類別
class myApp(wx.App):
   
   # 覆載OnInit()方法
   def OnInit(self):
      frame = myFrame(title="視窗", pos=(100,150), size=(250, 200))
      frame.Show()
      self.SetTopWindow(frame)
      return True

# 建立myFrame類別並繼承wx.Frame類別
class myFrame(wx.Frame):
   # 定義__init__()函數
   def __init__(self, title, pos, size):
      wx.Frame.__init__(self, None, -1, title, pos, size)

      # 建立狀態列
      self.CreateStatusBar()
      self.SetStatusText("這是狀態列")

# 定義main()函數
def main():
   # 建立myApp實例
   app = myApp()
   # 建立應用程式
   app.MainLoop()

if __name__ == "__main__":
   main()
