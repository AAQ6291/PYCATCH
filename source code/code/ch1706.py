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
      # �]�w�}���ɮ׮ɪ����ɦW�L�o�W��
      wildcard = "Python�ɮ� (*.py)|*.py|�Ҧ��ɮ� (*.*)|*.*"

      # �w�qwx.FileDialog���
      dlg = wx.FileDialog(
         self, message="�п���ɮ�", defaultDir="",
         defaultFile="", wildcard=wildcard, style=wx.OPEN | wx.MULTIPLE
         )

      # �p�G���UFileDialog�����}�ҫ��s
      if dlg.ShowModal() == wx.ID_OK:

         """
         �p�G�O����ɮץi�H�ϥ�GetPath()��ƨ��o��ܪ��ɮצW��,
         �]���ڭ̦bstyle�޼Ƹ̨ϥ�wx.MULTIPLE��ܥi�H�ɮצh��,
         Ū���h���ɮ׫h�O�ϥ�GetPaths()���.
         """
         paths = dlg.GetPaths()
         for path in paths:
            wx.MessageBox(path,"�A��ܪ��ɮ�")

      # Destroy FileDialog
      dlg.Destroy()


def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()
