#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入ConfigParser模組
import configparser

# 建立config instance
config = configparser.ConfigParser()

# 讀取ini file
config.read("./my-large.ini")

# 列出所有的section
print(config.sections())
