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
         '�ưʾ� Slider',
         size=(330, 350))

      # �إ�panel
      panel = wx.Panel(self, -1)

      # �إ߫����ưʾ��]Slider�^����
      slider = wx.Slider(
         panel,
         -1,
         5,
         1,
         100,
         pos=(10,10),
         size=(250, -1),
         style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

      # �]�w�ưʾ������
      slider.SetTickFreq(4, 1)

      # �إߤ����ưʾ��]Slider�^����
      slider = wx.Slider(
         panel,
         -1,
         25,
         1,
         100,
         pos=(125, 50),
         size=(-1, 250),
         style=wx.SL_VERTICAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

      # �]�w�ưʾ������
      slider.SetTickFreq(20, 1)


def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()

