#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入wx模組
import wx

# 建立myApp類別並繼承wx.App類別
class myApp(wx.App):
   
   # 覆載OnInit()方法, 這是程式的初始函數
   def OnInit(self): 
      """
      建立wx.Frame實例
      parent引數 - 這是window parent,通常設為None,
      如果這個引數不為None則Frame會一直在最上層視窗。
      title引數 - 視窗標題
      size引數 - 視窗大小
      """
      frame = wx.Frame(parent=None, title="測試", size=(250, 300))
      
      # 顯示frame
      frame.Show()
      return True
   
   # 覆載OnExit()方法.
   def OnExit(self):
      
      # 顯示訊息視窗
      wx.MessageBox("程式關閉", "訊息")

# 建立實例   
app = myApp()

# 執行程式
app.MainLoop()
