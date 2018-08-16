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

      # �إ�Panel
      panel = wx.Panel(self)
      # �s�W�@�ӫ��s�ñN���s�[�JPanel
      button = wx.Button(panel, label = "���s1", pos=(25, 25), size=(60, 25))

      # �إߨƥ��ť
      self.Bind(wx.EVT_CLOSE, self.OnCloseWin)
      self.Bind(wx.EVT_BUTTON, self.OnClick, button)
      
   # �w�qOnClick()���
   def OnClick(self, event):
      wx.MessageBox("�A���F���s","���ܰT��")

   # �w�qOnCloseWin()���
   def OnCloseWin(self, event):
      dlg = wx.MessageDialog(None, "�T�w�n�����{��?","���ܰT��", wx.YES_NO)
      # �p�G���UYES�~�|��������
      if dlg.ShowModal() == wx.ID_YES:
         self.Destroy()
      

# �w�qmain()���
def main():
   # �إ�myApp���
   app = myApp()
   # �إ����ε{��
   app.MainLoop()

if __name__ == "__main__":
   main()
