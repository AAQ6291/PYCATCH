#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwx�Ҳ�
import wx

# �w�qmyFrame���~��wx.Frame���O
class myFrame(wx.Frame):
   def __init__(self):
      wx.Frame.__init__(self, None, -1, '��r��줸��', size=(350, 150))
      panel = wx.Panel(self, -1)

      # �]�w����
      label1 = wx.StaticText(panel, -1, "����1")

      # �]�w��r���
      text1 = wx.TextCtrl(panel, -1, "�w�]��r", size=(200, -1))

      # �]�w����
      label2 = wx.StaticText(panel, -1, "����2")

      # �]�w�o�����O�K�X���
      text2 = wx.TextCtrl(panel, -1, "1234567890", size=(200, 32), style=wx.TE_PASSWORD)

      """
      FlexGridSizer���O
      �i���Y�ʪ�Grid sizer, �i�H�N�������@�Ӫ��e��, �D�n�O�������ڭ̦۰ʽs�Ƥ���,
      �åB�ڭ̥i�H�N�����J�o�Ӫ��e����.
      """
      sizer = wx.FlexGridSizer(cols=2, vgap=5, hgap=8)
      sizer.AddMany([label1, text1, label2, text2])
      panel.SetSizer(sizer)


if __name__ == "__main__":
   app = wx.PySimpleApp()
   frame = myFrame()
   frame.Show()
   app.MainLoop()

