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
         '��r��줸��',
         size=(400, 450))
      
      panel = wx.Panel(self, -1)
      
      # �s�W����
      label1 = wx.StaticText(panel, -1, "�h�����")

      # �s�W�h�����]multi-line�^
      text1 = wx.TextCtrl(
         panel,
         -1,
         "��1��...\n"
         "��2��...\n"
         "��3��...",
         size = (300,200),
         style = wx.TE_MULTILINE)

      # �s�W����
      label2 = wx.StaticText(panel, -1, "RichText���")

      # �s�WRichText���
      text2 = wx.TextCtrl(
         panel,
         -1,
         "",
         size = (300, 200),
         style = wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_AUTO_URL|wx.TE_LINEWRAP)

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

