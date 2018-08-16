#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwx�Ҳ�
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
   <title>�ϥ�wxPythonŪ��HTML</title>

   </head>

   <body>
   <h2>�o�OHTML�y�k
   </h2>
   <table width="27%"  border="1" cellspacing="1" cellpadding="3">
     <tr>
       <td width="28%">�x�s��1</td>
       <td width="72%">�x�s��2</td>
     </tr>
     <tr>
       <td>�x�s��3</td>
       <td>�x�s��4</td>
     </tr>
   </table>
   <font color="#993300" size="+5">��r1</font><br>
   ��r2<br>
   <font color="#0000CC" size="+7">��r3</font>
   </body>
   </html>
   """

   def __init__(self, parent, id):
      wx.Frame.__init__(self, parent, id, '�u��C', size=(500, 500))

      wxhtml = wx.html.HtmlWindow(self)
      wxhtml.SetPage(self.html)



def main():
   app = myApp()
   app.MainLoop()
   
if __name__ == "__main__":
   main()
