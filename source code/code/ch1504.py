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
      self.label.Text = "�h�ﶵ�ر���]CheckBox�^"
      self.label.Location = Point(15, 25)
      self.label.AutoSize = True

      # �إ� CheckBox1
      self.check1 = CheckBox()
      self.check1.Text = "���1"
      self.check1.Location = Point(15, 50)
      self.check1.Width = 60

      # �إ� CheckBox2
      self.check2 = CheckBox()
      self.check2.Text = "���2"
      self.check2.Location = Point(85, 50)
      self.check2.Width = 60
      self.check2.Checked = True

      # �إ� CheckBox3
      self.check3 = CheckBox()
      self.check3.Text = "���3"
      self.check3.Location = Point(145, 50)
      self.check3.Width = 60

      #�@�N��������[�J��������C��
      self.Controls.Add(self.label)
      self.Controls.Add(self.check1)
      self.Controls.Add(self.check2)
      self.Controls.Add(self.check3)

# ����myForm()���O
Application.Run(myForm())
