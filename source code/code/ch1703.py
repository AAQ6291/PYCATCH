#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwx�Ҳ�
import wx

# �إ�myApp���O���~��wx.App���O
class myApp(wx.App):
   
   # �и�OnInit()��k
   def OnInit(self):
      frame = myFrame(title="����", pos=(100,150), size=(250, 200))
      frame.Show()
      self.SetTopWindow(frame)
      return True

# �إ�myFrame���O���~��wx.Frame���O
class myFrame(wx.Frame):
   # �w�q__init__()���
   def __init__(self, title, pos, size):
      wx.Frame.__init__(self, None, -1, title, pos, size)

      # �إߪ��A�C
      self.CreateStatusBar()
      self.SetStatusText("�o�O���A�C")

# �w�qmain()���
def main():
   # �إ�myApp���
   app = myApp()
   # �إ����ε{��
   app.MainLoop()

if __name__ == "__main__":
   main()
