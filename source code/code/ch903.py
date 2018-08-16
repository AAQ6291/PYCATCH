#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入ConfigParser模組
import ConfigParser

# 建立config instance
config = ConfigParser.ConfigParser()

# 讀取ini file
config.read("./my-large.ini")

# 列出所有的section
print config.sections()
