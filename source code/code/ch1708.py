#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入wx模組
import wx

# 定義myFrame並繼承wx.Frame類別
class myFrame(wx.Frame):
   def __init__(self):
      wx.Frame.__init__(self, None, -1, '文字欄位元件', size=(350, 150))
      panel = wx.Panel(self, -1)

      # 設定標籤
      label1 = wx.StaticText(panel, -1, "標籤1")

      # 設定文字欄位
      text1 = wx.TextCtrl(panel, -1, "預設文字", size=(200, -1))

      # 設定標籤
      label2 = wx.StaticText(panel, -1, "標籤2")

      # 設定這個欄位是密碼欄位
      text2 = wx.TextCtrl(panel, -1, "1234567890", size=(200, 32), style=wx.TE_PASSWORD)

      """
      FlexGridSizer類別
      可伸縮性的Grid sizer, 可以將它視為一個表格容器, 主要是它能幫我們自動編排元件,
      並且我們可以將元件放入這個表格容器內.
      """
      sizer = wx.FlexGridSizer(cols=2, vgap=5, hgap=8)
      sizer.AddMany([label1, text1, label2, text2])
      panel.SetSizer(sizer)


if __name__ == "__main__":
   app = wx.PySimpleApp()
   frame = myFrame()
   frame.Show()
   app.MainLoop()

