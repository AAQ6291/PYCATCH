#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwx�Ҳ�
import wx

# �w�qmyFrame���~��wx.Frame���O
class myFrame(wx.Frame):
   def __init__(self):
      wx.Frame.__init__(
         self,
         None,
         -1,
         '�Ϲ����s',
         size=(350, 250))

      # �إ�panel
      panel = wx.Panel(self, -1)

      # Ū���Ĥ@�ӹϤ���
      bmp = wx.Image("button1.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

      # �إ߫��s1, �ñN���s�[��panel�W
      self.button = wx.BitmapButton(
         panel,
         -1,
         bmp,
         size = (90, 70),
         pos=(30,30))

      # Ū���ĤG�ӹϤ���
      bmp1 = wx.Image("button2.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

      # �إ߫��s2, �ñN���s�[��panel�W
      self.button1 = wx.BitmapButton(
         panel,
         -1,
         bmp1,
         size = (90, 70),
         pos=(140,30))

      """
      ��ťĲ�o�ƥ�
      ����ӫ��s1�|Ĳ�oOnClick1���
      ����ӫ��s2�|Ĳ�oOnClick2���
      """
      self.Bind(wx.EVT_BUTTON, self. OnClick1, self.button)
      self.Bind(wx.EVT_BUTTON, self. OnClick2, self.button1)

   def OnClick1(self, event):
      wx.MessageBox("�A���U�F���s1")
      
   def OnClick2(self, event):
      wx.MessageBox("�A���U�F���s2")

if __name__ == "__main__":
   app = wx.PySimpleApp()
   frame = myFrame()
   frame.Show()
   app.MainLoop()

