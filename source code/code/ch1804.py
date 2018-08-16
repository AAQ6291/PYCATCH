#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入win32com.client模組
import win32com.client

# 建立Excel
app = win32com.client.Dispatch("Excel.Application")

# 顯示Excel
app.Visible = 1

# 建立Excel
workbook = app.Workbooks.Add()

# 建立工作表
sheet = workbook.Sheets.Add()

# 產生9x9的表格
for i in xrange(2, 10):
   # Cells(<column>, <row>)
   sheet.Cells(1, i).Value = i
   sheet.Cells(1, i).Font.Color = 0x008800
   sheet.Cells(i, 1).Value = i
   sheet.Cells(i, 1).Font.Color = 0x660000

# 將數字轉換為字串,因為要取得欄位名稱    
def IntToStr(i):
   return chr((i-1) + ord('A'))
    
for i in xrange(2, 10):
   for j in xrange(2, 10):
      # 建立計算公式
      sheet.Cells(i, j).Formula = '=%s1*A%s' % (IntToStr(j), i)
      sheet.Cells(i, j).Font.Color = 0x336600

# 設定工作表名稱
sheet.Name = "九久乘法表"

# 存檔
workbook.SaveAs('c:\\ch1804.xls')

# 結果程序
app.Quit()
