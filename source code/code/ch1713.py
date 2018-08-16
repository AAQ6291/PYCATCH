#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入wx模組
import wx

class myApp(wx.App):
   def OnInit(self):
      frame = myFrame()
      frame.Show()
      return True
   
# 定義myFrame並繼承wx.Frame類別
class myFrame(wx.Frame):
   def __init__(self):
      wx.Frame.__init__(
         self,
         None,
         -1,
         'Progress Bar',
         size=(320, 150))

      # 建立panel
      panel = wx.Panel(self, -1)

      # 計算目前進度的count變數
      self.count = 0

      # 建立 Progress Bar元件
      self.gauge = wx.Gauge(
         panel,
         -1,
         50,
         pos = (5, 50),
         size = (300, 20),
         style=wx.GA_HORIZONTAL)

      # 監聽事件
      self.Bind(wx.EVT_IDLE, self.OnIdle)

   # OnIdle事件函數
   def OnIdle(self, event):
      self.count += 1
      if self.count >= 100:
         self.count = 0

      # 更新進度
      self.gauge.SetValue(self.count)


def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()

