# -*- coding: cp950 -*-

# 載入awt
from java import awt

# 建立子類別（SubClass）
class SpamListener(awt.event.ActionListener):
   # 事件函數
   def actionPerformed(self,event):
      # 如果按下按鈕就執行print
      if event.getActionCommand() == "button":
         print '你按下按鈕'

# 建立instance
f = awt.Frame("ch1603", size=(250,150))

# 建立一個awt按鈕
b = awt.Button("button")

# 監聽事件
b.addActionListener(SpamListener())

# 將按鈕加入
f.add(b, "Center")

# 顯示Frame
f.setVisible(1)
