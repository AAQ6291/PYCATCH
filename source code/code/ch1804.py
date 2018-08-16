#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwin32com.client�Ҳ�
import win32com.client

# �إ�Excel
app = win32com.client.Dispatch("Excel.Application")

# ���Excel
app.Visible = 1

# �إ�Excel
workbook = app.Workbooks.Add()

# �إߤu�@��
sheet = workbook.Sheets.Add()

# ����9x9�����
for i in xrange(2, 10):
   # Cells(<column>, <row>)
   sheet.Cells(1, i).Value = i
   sheet.Cells(1, i).Font.Color = 0x008800
   sheet.Cells(i, 1).Value = i
   sheet.Cells(i, 1).Font.Color = 0x660000

# �N�Ʀr�ഫ���r��,�]���n���o���W��    
def IntToStr(i):
   return chr((i-1) + ord('A'))
    
for i in xrange(2, 10):
   for j in xrange(2, 10):
      # �إ߭p�⤽��
      sheet.Cells(i, j).Formula = '=%s1*A%s' % (IntToStr(j), i)
      sheet.Cells(i, j).Font.Color = 0x336600

# �]�w�u�@��W��
sheet.Name = "�E�[���k��"

# �s��
workbook.SaveAs('c:\\ch1804.xls')

# ���G�{��
app.Quit()
