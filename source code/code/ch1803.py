#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwin32com.client�Ҳ�
import win32com.client

# �إ߷s��Word����
app = win32com.client.Dispatch("Word.Application")

"""
�NWord���ε{������, �N��O�U���ڭ̹�WORD���ާ@���n�H�I���覡�B�z.
0 = ����
1 = ���
"""
app.Visible = 1

# �إ߷s�����
doc = app.Documents.Add()

# �g�J��r
doc.Content.Text = "�o�O��Python�إߪ�Word���P���e!!!"

# �s��
doc.SaveAs("c:\\ch1803.doc")

# ����Word
doc.Close()
# �����{��
app.Quit()
