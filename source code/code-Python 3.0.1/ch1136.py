#!/usr/bin/env python
#coding=utf-8

# 載入urllib.robotparser模組
import urllib.robotparser

# 建立instance
robot = urllib.robotparser.RobotFileParser()

# 設定要讀取的robots位置
robot.set_url("http://www.google.com/robots.txt")

# 讀取
robot.read()

# 查看這個網址是否允許robots讀取
print("http://www.google.com/news?output=xhtml& = ", robot.can_fetch("*","http://www.google.com/news?output=xhtml&"))

# 查看這個網址是否允許robots讀取
print("http://www.google.com/ = ", robot.can_fetch("*","http://www.google.com/"))

# 查看這個網址是否允許robots讀取
print("http://www.google.com/searchhistory/ = ", robot.can_fetch("*","http://www.google.com/searchhistory/"))

