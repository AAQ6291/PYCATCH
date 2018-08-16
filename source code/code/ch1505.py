# -*- coding: cp950 -*-

# 載入clr模組
import clr

# 參考System.Windows.Forms與System.Drawing
clr.AddReference("System.Windows.Forms")
clr.AddReference('System.Drawing')

# 載入System.Windows.Forms.*模組
from System.Windows.Forms import *
from System.Drawing import *

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

      # 視窗的大小
      self.Width = 350
      self.Height = 200

      # 建立 Label
      self.label = Label()
      self.label.Text = "單選項目控件（RadioButton）"
      self.label.Location = Point(15, 25)
      self.label.AutoSize = True

      self.radio1 = RadioButton()
      self.radio1.Text = "蘋果"
      self.radio1.Location = Point(15, 55)
      self.radio1.Checked = True

      self.radio2 = RadioButton()
      self.radio2.Text = "橘子"
      self.radio2.Location = Point(120, 55)

      self.radio3 = RadioButton()
      self.radio3.Text = "西瓜"
      self.radio3.Location = Point(260, 55)


      #　將控件全部加入視窗控件列表
      self.Controls.Add(self.label)
      self.Controls.Add(self.radio1)
      self.Controls.Add(self.radio2)
      self.Controls.Add(self.radio3)

# 執行myForm()類別
Application.Run(myForm())
