#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���JSendKeys�Ҳ�
import SendKeys

# �ϥ�SendKeys�}�ҵ��O���ÿ�J��r
SendKeys.SendKeys("""
{LWIN}
{PAUSE .50}
r
notepad.exe{ENTER}
{PAUSE 1}
Hello{ENTER}
^{SPACE}
su31
cl31
{SPACE}
5k41
g42
m/41
^{SPACE}
Python
^{SPACE}
y41
+5
cj842
283
y42^
{SPACE}... 
^s
c:\python-sendkeys.txt
%s
""")
