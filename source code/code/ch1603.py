# -*- coding: cp950 -*-

# ���Jawt
from java import awt

# �إߤl���O�]SubClass�^
class SpamListener(awt.event.ActionListener):
   # �ƥ���
   def actionPerformed(self,event):
      # �p�G���U���s�N����print
      if event.getActionCommand() == "button":
         print '�A���U���s'

# �إ�instance
f = awt.Frame("ch1603", size=(250,150))

# �إߤ@��awt���s
b = awt.Button("button")

# ��ť�ƥ�
b.addActionListener(SpamListener())

# �N���s�[�J
f.add(b, "Center")

# ���Frame
f.setVisible(1)
