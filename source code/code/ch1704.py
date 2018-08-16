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

      # 建立Panel
      panel = wx.Panel(self)
      # 新增一個按鈕並將按鈕加入Panel
      button = wx.Button(panel, label = "按鈕1", pos=(25, 25), size=(60, 25))

      # 建立事件監聽
      self.Bind(wx.EVT_CLOSE, self.OnCloseWin)
      self.Bind(wx.EVT_BUTTON, self.OnClick, button)
      
   # 定義OnClick()函數
   def OnClick(self, event):
      wx.MessageBox("你按了按鈕","提示訊息")

   # 定義OnCloseWin()函數
   def OnCloseWin(self, event):
      dlg = wx.MessageDialog(None, "確定要關閉程式?","提示訊息", wx.YES_NO)
      # 如果按下YES才會關閉視窗
      if dlg.ShowModal() == wx.ID_YES:
         self.Destroy()
      

# 定義main()函數
def main():
   # 建立myApp實例
   app = myApp()
   # 建立應用程式
   app.MainLoop()

if __name__ == "__main__":
   main()
