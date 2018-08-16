#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwx�Ҳ�
import wx

class myApp(wx.App):
   def OnInit(self):
      frame = myToolBarFrame(parent=None, id=-1)
      frame.Show()
      return True
      
class myToolBarFrame(wx.Frame):
   def __init__(self, parent, id):
      wx.Frame.__init__(self, parent, id, '�u��C', size=(300, 200))
      panel = wx.Panel(self)

      # �إ�wx.ToolBar���
      self.toolbar = wx.ToolBar(self, id=-1, size=(20,20), style=wx.TB_TEXT)

      # �s�WToolBar�����s
      self.toolbar.AddLabelTool(1, '�s�W', wx.Bitmap('file.gif'), wx.NullBitmap, wx.ITEM_NORMAL, "�}�ҷs�ɮ�")

      # ���j�u
      self.toolbar.AddSeparator()

      # �s�WToolBar�����s
      self.toolbar.AddLabelTool(2, '�}��', wx.Bitmap('openfolder.gif'), wx.NullBitmap, wx.ITEM_NORMAL, "�}�����ɮ�")

      # ��{ToolBar
      self.toolbar.Realize()

      # �w�mToolBar
      self.SetToolBar(self.toolbar)

      # �إ�ToolBar���ƥ��ť
      self.Bind(wx.EVT_TOOL, self.OnEvent1, id=1)
      self.Bind(wx.EVT_TOOL, self.OnEvent2, id=2)

   def OnEvent1(self, event):
      wx.MessageBox("�A���U�F�s�W���s", "�T������")

   def OnEvent2(self, event):
      wx.MessageBox("�A���U�F�}�ҫ��s", "�T������")

def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()
