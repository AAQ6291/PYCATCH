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
      # wx.NewId()是wxPython ID號碼.
      id = wx.NewId()
      # wx.Frame.__init__()函數
      wx.Frame.__init__(self, None, id, title, pos, size)

      # 建立wx.Menu實例
      menu = wx.Menu()

      # 設定Menu的內容
      menu.Append(1, "關於")

      # Menu分隔線
      menu.AppendSeparator()

      # 設定Menu的內容
      menu.Append(2, "E&xit")

      # 建立wx.MenuBar實例
      menuBar = wx.MenuBar()

      # 將menu加入menuBar
      menuBar.Append(menu, "檔案")

      # 告訴Frame要設定的MenuBar是menuBar實例
      self.SetMenuBar(menuBar)

# 定義main()函數
def main():
   # 建立myApp實例
   app = myApp()
   # 建立應用程式
   app.MainLoop()

if __name__ == "__main__":
   main()
