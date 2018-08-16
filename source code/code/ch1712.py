#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwx�Ҳ�
import wx

class myApp(wx.App):
   def OnInit(self):
      frame = myFrame()
      frame.Show()
      return True
   
# �w�qmyFrame���~��wx.Frame���O
class myFrame(wx.Frame):
   def __init__(self):
      wx.Frame.__init__(
         self,
         None,
         -1,
         'Up/Down���s',
         size=(300, 150))

      # �إ�panel
      panel = wx.Panel(self, -1)

      # �إ�up/down���s
      spinctrl = wx.SpinCtrl(
         panel,
         -1,
         pos=(10, 20),
         size=(60, -1))

      # �]�w�̤p�ȻP�̤j��
      spinctrl.SetRange(0, 100)

      # �]�w�@�}�l����
      spinctrl.SetValue(10)

      # �إ�up/down���s
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

