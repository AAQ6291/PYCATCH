# -*- coding: cp950 -*-

# ���Jclr�Ҳ�
import clr

# �Ѧ�System.Windows.Forms
clr.AddReference("System.Windows.Forms")

# ���JSystem.Windows.Forms.*�Ҳ�
from System.Windows.Forms import *

# �إߦۭq���O���~��Form���O
class myForm(Form):

   """
    __init__(self)��ƬO��l,
   �ڭ̥i�H�N�@�ǻݭn�{���@�}�l�N�|���檺���e��J�o�Ө�Ƥ�/
   """
   def __init__(self):

      # ���������D��r
      self.Text = "�ڪ��Ĥ@��.NET����"

# ����myForm()���O
Application.Run(myForm())
