#!/usr/bin/env python
#coding=utf-8

# 載入os模組
import os

# 顯示系統名稱
print "OS name = ", os.name

# 顯示系統環境值
for key in os.environ:
   print "key = %s \t\t\t\t value = %s" % (key, os.environ[key])


# 使用os.system(cmd)函數執行Windows命令提示字元指令.
print os.system("cmd.exe | dir c:\\tmp111")

