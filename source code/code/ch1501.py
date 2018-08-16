# -*- coding: cp950 -*-

# 載入clr模組
import clr

# 參考System.Windows.Forms
clr.AddReference("System.Windows.Forms")

# 載入System.Windows.Forms.*模組
from System.Windows.Forms import *

# 建立自訂類別並繼承Form類別
class myForm(Form):

   """
    __init__(self)函數是初始,
   我們可以將一些需要程式一開始就會執行的內容放入這個函數內/
   """
   def __init__(self):

      # 視窗的標題文字
      self.Text = "我的第一個.NET視窗"

# 執行myForm()類別
Application.Run(myForm())
