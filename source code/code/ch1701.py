#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwx�Ҳ�
import wx

# �إ�myApp���O���~��wx.App���O
class myApp(wx.App):
   
   # �и�OnInit()��k, �o�O�{������l���
   def OnInit(self): 
      """
      �إ�wx.Frame���
      parent�޼� - �o�Owindow parent,�q�`�]��None,
      �p�G�o�Ӥ޼Ƥ���None�hFrame�|�@���b�̤W�h�����C
      title�޼� - �������D
      size�޼� - �����j�p
      """
      frame = wx.Frame(parent=None, title="����", size=(250, 300))
      
      # ���frame
      frame.Show()
      return True
   
   # �и�OnExit()��k.
   def OnExit(self):
      
      # ��ܰT������
      wx.MessageBox("�{������", "�T��")

# �إ߹��   
app = myApp()

# ����{��
app.MainLoop()
