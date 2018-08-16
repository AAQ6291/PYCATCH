#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入wx模組
import wx

# 定義myFrame並繼承wx.Frame類別
class myFrame(wx.Frame):
   def __init__(self):
      wx.Frame.__init__(
         self,
         None,
         -1,
         '圖像按鈕',
         size=(350, 250))

      # 建立panel
      panel = wx.Panel(self, -1)

      # 讀取第一個圖片檔
      bmp = wx.Image("button1.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

      # 建立按鈕1, 並將按鈕加到panel上
      self.button = wx.BitmapButton(
         panel,
         -1,
         bmp,
         size = (90, 70),
         pos=(30,30))

      # 讀取第二個圖片檔
      bmp1 = wx.Image("button2.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

      # 建立按鈕2, 並將按鈕加到panel上
      self.button1 = wx.BitmapButton(
         panel,
         -1,
         bmp1,
         size = (90, 70),
         pos=(140,30))

      """
      監聽觸發事件
      當按照按鈕1會觸發OnClick1函數
      當按照按鈕2會觸發OnClick2函數
      """
      self.Bind(wx.EVT_BUTTON, self. OnClick1, self.button)
      self.Bind(wx.EVT_BUTTON, self. OnClick2, self.button1)

   def OnClick1(self, event):
      wx.MessageBox("你按下了按鈕1")
      
   def OnClick2(self, event):
      wx.MessageBox("你按下了按鈕2")

if __name__ == "__main__":
   app = wx.PySimpleApp()
   frame = myFrame()
   frame.Show()
   app.MainLoop()

