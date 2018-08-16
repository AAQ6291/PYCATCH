#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入win32com.client模組
import win32com.client

# 建立新的Word物件
app = win32com.client.Dispatch("Word.Application")

"""
將Word應用程式隱藏, 意思是下面我們對WORD的操作都要以背景方式處理.
0 = 隱藏
1 = 顯示
"""
app.Visible = 1

# 建立新的文件
doc = app.Documents.Add()

# 寫入文字
doc.Content.Text = "這是用Python建立的Word文件與內容!!!"

# 存檔
doc.SaveAs("c:\\ch1803.doc")

# 關閉Word
doc.Close()
# 結束程序
app.Quit()
