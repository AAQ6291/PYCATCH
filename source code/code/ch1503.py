# -*- coding: cp950 -*-

# ���Jclr�Ҳ�
import clr

# �Ѧ�System.Windows.Forms
clr.AddReference("System.Windows.Forms")

# ���JSystem.Windows.Forms.*�Ҳ�
from System.Windows.Forms import *

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

      # �إߤ@�ӫ��s
      button = Button(Text="�T������", Left=100, Top=150)

      # �ŧi���s�ƥ�, �I����|�I�sself.OnButtonClick���
      button.Click += self.OnButtonClick

      # �إ߼��ҡ]Label�^
      self.label = Label(Text="�п�J�T��:", Left=10, Top=10)

      # �إ�TextBox
      self.textbox = TextBox(Left=110, Top=10)

      # �N���s,Label�PTextBox�[�J����������C��.
      self.Controls.Add(button)
      self.Controls.Add(self.label)
      self.Controls.Add(self.textbox)
      
   # �w�qOnButtonClick()���, ���I���ƥ�o�ͫ�|�I�s�����.
   def OnButtonClick(self, *args):
      
      # �I�sMessageBox����, �ñ���textbox��J����
      MessageBox.Show(self.textbox.Text,"�o�O�T������ MessageBox")

# ����myForm()���O
Application.Run(myForm())
