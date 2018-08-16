#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入SendKeys模組
import SendKeys

"""
使用SendKeys開啟瀏覽器並輸入www.google.com網址後再輸入python關鍵字搜尋
"""
SendKeys.SendKeys("""
{LWIN}
{PAUSE .50}
r
IEXPLORE.EXE{ENTER}
{PAUSE 5}
%d
www.google.com{ENTER}
{PAUSE 5}
python{ENTER}
{PAUSE 3}
{DOWN 5}
""")
