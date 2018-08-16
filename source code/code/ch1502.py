# -*- coding: cp950 -*-

# 載入clr模組
import clr

# 參考System.Windows.Forms
clr.AddReference("System.Windows.Forms")

# 載入System.Windows.Forms.*模組
from System.Windows.Forms import *

"""
建立自訂類別並繼承Form類別,
因為繼承, 所以myForm擁有Form的所有特性
"""
class myForm(Form):

   """
    __init__(self)函數(方法)是初始,
   我們可以將一些需要程式一開始就會執行的內容放入這個函數內
   """
   def __init__(self):

      # 視窗的標題文字
      self.Text = "我的.NET視窗"

      # 建立一個按鈕
      button = Button(Text="訊息視窗", Left=100, Top=150)

      # 宣告按鈕事件, 點擊後會呼叫self.OnButtonClick函數
      button.Click += self.OnButtonClick

      # 將按鈕加入視窗的控件列表內.
      self.Controls.Add(button)

   # 定義OnButtonClick()函數, 當點擊事件發生後會呼叫此函數.
   def OnButtonClick(self, *args):
      
      # 呼叫MessageBox視窗
      MessageBox.Show("這是訊息視窗 MessageBox")

# 執行myForm()類別
Application.Run(myForm())
