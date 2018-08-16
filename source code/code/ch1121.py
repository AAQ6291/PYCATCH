#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入getopt模組
import getopt

# 取得使用者的參數
args = "-h 192.168.1.1 -p 8080 -u user -s 1234 -x -y".split()

# 利用getopt.getopt()函數來處理
optlist, args = getopt.getopt(args, 'h:p:u:s:xy')

# 輸出結果
print optlist

