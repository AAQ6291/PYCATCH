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
         '文字欄位元件',
         size=(400, 450))
      
      panel = wx.Panel(self, -1)
      
      # 新增標籤
      label1 = wx.StaticText(panel, -1, "多行欄位")

      # 新增多行欄位（multi-line）
      text1 = wx.TextCtrl(
         panel,
         -1,
         "第1行...\n"
         "第2行...\n"
         "第3行...",
         size = (300,200),
         style = wx.TE_MULTILINE)

      # 新增標籤
      label2 = wx.StaticText(panel, -1, "RichText欄位")

      # 新增RichText欄位
      text2 = wx.TextCtrl(
         panel,
         -1,
         "",
         size = (300, 200),
         style = wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_AUTO_URL|wx.TE_LINEWRAP)

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

