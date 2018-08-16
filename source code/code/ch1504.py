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
      self.label.Text = "多選項目控件（CheckBox）"
      self.label.Location = Point(15, 25)
      self.label.AutoSize = True

      # 建立 CheckBox1
      self.check1 = CheckBox()
      self.check1.Text = "選擇1"
      self.check1.Location = Point(15, 50)
      self.check1.Width = 60

      # 建立 CheckBox2
      self.check2 = CheckBox()
      self.check2.Text = "選擇2"
      self.check2.Location = Point(85, 50)
      self.check2.Width = 60
      self.check2.Checked = True

      # 建立 CheckBox3
      self.check3 = CheckBox()
      self.check3.Text = "選擇3"
      self.check3.Location = Point(145, 50)
      self.check3.Width = 60

      #　將控件全部加入視窗控件列表
      self.Controls.Add(self.label)
      self.Controls.Add(self.check1)
      self.Controls.Add(self.check2)
      self.Controls.Add(self.check3)

# 執行myForm()類別
Application.Run(myForm())
