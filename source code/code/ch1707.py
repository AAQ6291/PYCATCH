#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入wx模組
import wx
import wx.html

class myApp(wx.App):
   def OnInit(self):
      frame = myHTMLFrame(parent=None, id=-1)
      frame.Show()
      return True

class myHTMLFrame(wx.Frame):
   html = """
   <html>
   <head>
   <meta http-equiv="Content-Type" content="text/html; charset=big5">
   <title>使用wxPython讀取HTML</title>

   </head>

   <body>
   <h2>這是HTML語法
   </h2>
   <table width="27%"  border="1" cellspacing="1" cellpadding="3">
     <tr>
       <td width="28%">儲存格1</td>
       <td width="72%">儲存格2</td>
     </tr>
     <tr>
       <td>儲存格3</td>
       <td>儲存格4</td>
     </tr>
   </table>
   <font color="#993300" size="+5">文字1</font><br>
   文字2<br>
   <font color="#0000CC" size="+7">文字3</font>
   </body>
   </html>
   """

   def __init__(self, parent, id):
      wx.Frame.__init__(self, parent, id, '工具列', size=(500, 500))

      wxhtml = wx.html.HtmlWindow(self)
      wxhtml.SetPage(self.html)



def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()
