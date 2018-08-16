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
      # wx.NewId()�OwxPython ID���X.
      id = wx.NewId()
      # wx.Frame.__init__()���
      wx.Frame.__init__(self, None, id, title, pos, size)

      # �إ�wx.Menu���
      menu = wx.Menu()

      # �]�wMenu�����e
      menu.Append(1, "����")

      # Menu���j�u
      menu.AppendSeparator()

      # �]�wMenu�����e
      menu.Append(2, "E&xit")

      # �إ�wx.MenuBar���
      menuBar = wx.MenuBar()

      # �Nmenu�[�JmenuBar
      menuBar.Append(menu, "�ɮ�")

      # �i�DFrame�n�]�w��MenuBar�OmenuBar���
      self.SetMenuBar(menuBar)

# �w�qmain()���
def main():
   # �إ�myApp���
   app = myApp()
   # �إ����ε{��
   app.MainLoop()

if __name__ == "__main__":
   main()
