#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���JSendKeys�Ҳ�
import SendKeys

"""
�ϥ�SendKeys�}���s�����ÿ�Jwww.google.com���}��A��Jpython����r�j�M
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
