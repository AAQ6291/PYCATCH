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
         'Up/Down按鈕',
         size=(300, 150))

      # 建立panel
      panel = wx.Panel(self, -1)

      # 建立up/down按鈕
      spinctrl = wx.SpinCtrl(
         panel,
         -1,
         pos=(10, 20),
         size=(60, -1))

      # 設定最小值與最大值
      spinctrl.SetRange(0, 100)

      # 設定一開始的值
      spinctrl.SetValue(10)

      # 建立up/down按鈕
      spinctrl1 = wx.SpinCtrl(
         panel,
         id = -1,
         value = wx.EmptyString,
         pos = (10, 50),
         size = wx.DefaultSize,
         style = wx.SP_ARROW_KEYS|wx.SP_WRAP,
         min = 0,
         max = 100,
         initial = 0,
         name = "mySpinCtrl")

def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()

