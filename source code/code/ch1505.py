# -*- coding: cp950 -*-

# ���Jclr�Ҳ�
import clr

# �Ѧ�System.Windows.Forms�PSystem.Drawing
clr.AddReference("System.Windows.Forms")
clr.AddReference('System.Drawing')

# ���JSystem.Windows.Forms.*�Ҳ�
from System.Windows.Forms import *
from System.Drawing import *

"""
�إߦۭq���O���~��Form���O,
�]���~��, �ҥHmyForm�֦�Form���Ҧ��S��
"""
class myForm(Form):

   """
    __init__(self)���(��k)�O��l,
   �ڭ̥i�H�N�@�ǻݭn�{���@�}�l�N�|���檺���e��J�o�Ө�Ƥ�
   """
   def __init__(self):

      # ���������D��r
      self.Text = "�ڪ�.NET����"

      # �������j�p
      self.Width = 350
      self.Height = 200

      # �إ� Label
      self.label = Label()
      self.label.Text = "��ﶵ�ر���]RadioButton�^"
      self.label.Location = Point(15, 25)
      self.label.AutoSize = True

      self.radio1 = RadioButton()
      self.radio1.Text = "ī�G"
      self.radio1.Location = Point(15, 55)
      self.radio1.Checked = True

      self.radio2 = RadioButton()
      self.radio2.Text = "��l"
      self.radio2.Location = Point(120, 55)

      self.radio3 = RadioButton()
      self.radio3.Text = "���"
      self.radio3.Location = Point(260, 55)


      #�@�N��������[�J��������C��
      self.Controls.Add(self.label)
      self.Controls.Add(self.radio1)
      self.Controls.Add(self.radio2)
      self.Controls.Add(self.radio3)

# ����myForm()���O
Application.Run(myForm())
