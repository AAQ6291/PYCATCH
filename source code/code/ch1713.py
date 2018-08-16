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
         'Progress Bar',
         size=(320, 150))

      # �إ�panel
      panel = wx.Panel(self, -1)

      # �p��ثe�i�ת�count�ܼ�
      self.count = 0

      # �إ� Progress Bar����
      self.gauge = wx.Gauge(
         panel,
         -1,
         50,
         pos = (5, 50),
         size = (300, 20),
         style=wx.GA_HORIZONTAL)

      # ��ť�ƥ�
      self.Bind(wx.EVT_IDLE, self.OnIdle)

   # OnIdle�ƥ���
   def OnIdle(self, event):
      self.count += 1
      if self.count >= 100:
         self.count = 0

      # ��s�i��
      self.gauge.SetValue(self.count)


def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()

