#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入wx模組
import wx

class myApp(wx.App):
   def OnInit(self):
      frame = myToolBarFrame(parent=None, id=-1)
      frame.Show()
      return True
      
class myToolBarFrame(wx.Frame):
   def __init__(self, parent, id):
      wx.Frame.__init__(self, parent, id, '工具列', size=(300, 200))
      panel = wx.Panel(self)

      # 建立wx.ToolBar實例
      self.toolbar = wx.ToolBar(self, id=-1, size=(20,20), style=wx.TB_TEXT)

      # 新增ToolBar的按鈕
      self.toolbar.AddLabelTool(1, '新增', wx.Bitmap('file.gif'), wx.NullBitmap, wx.ITEM_NORMAL, "開啟新檔案")

      # 分隔線
      self.toolbar.AddSeparator()

      # 新增ToolBar的按鈕
      self.toolbar.AddLabelTool(2, '開啟', wx.Bitmap('openfolder.gif'), wx.NullBitmap, wx.ITEM_NORMAL, "開啟舊檔案")

      # 實現ToolBar
      self.toolbar.Realize()

      # 安置ToolBar
      self.SetToolBar(self.toolbar)

      # 建立ToolBar的事件監聽
      self.Bind(wx.EVT_TOOL, self.OnEvent1, id=1)
      self.Bind(wx.EVT_TOOL, self.OnEvent2, id=2)

   def OnEvent1(self, event):
      wx.MessageBox("你按下了新增按鈕", "訊息視窗")

   def OnEvent2(self, event):
      # 設定開啟檔案時的副檔名過濾名稱
      wildcard = "Python檔案 (*.py)|*.py|所有檔案 (*.*)|*.*"

      # 定義wx.FileDialog實例
      dlg = wx.FileDialog(
         self, message="請選擇檔案", defaultDir="",
         defaultFile="", wildcard=wildcard, style=wx.OPEN | wx.MULTIPLE
         )

      # 如果按下FileDialog內的開啟按鈕
      if dlg.ShowModal() == wx.ID_OK:

         """
         如果是單選檔案可以使用GetPath()函數取得選擇的檔案名稱,
         因為我們在style引數裡使用wx.MULTIPLE表示可以檔案多選,
         讀取多選檔案則是使用GetPaths()函數.
         """
         paths = dlg.GetPaths()
         for path in paths:
            wx.MessageBox(path,"你選擇的檔案")

      # Destroy FileDialog
      dlg.Destroy()


def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()
