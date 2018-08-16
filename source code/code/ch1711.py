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
         '滑動器 Slider',
         size=(330, 350))

      # 建立panel
      panel = wx.Panel(self, -1)

      # 建立垂直滑動器（Slider）元件
      slider = wx.Slider(
         panel,
         -1,
         5,
         1,
         100,
         pos=(10,10),
         size=(250, -1),
         style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

      # 設定滑動器的刻度
      slider.SetTickFreq(4, 1)

      # 建立水平滑動器（Slider）元件
      slider = wx.Slider(
         panel,
         -1,
         25,
         1,
         100,
         pos=(125, 50),
         size=(-1, 250),
         style=wx.SL_VERTICAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

      # 設定滑動器的刻度
      slider.SetTickFreq(20, 1)


def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()

