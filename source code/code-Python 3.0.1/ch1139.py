#!/usr/bin/env python
#coding=utf-8

import string

text ="Python language"

print("將字串轉為大寫字母方法1: ", str.upper(text))
print("將字串轉為大寫字母方法2: ", text.upper())

print("將字串轉為小寫字母方法1: ", str.lower(text))
print("將字串轉為小寫字母方法2: ", text.lower())

print("將字串進行分割方法1: ", str.split(text))
print("將字串進行分割方法2: ", text.split())

print("使用join()函數方法: ", str.join(text, "|"))

print("使用replace()函數方法1: ", str.replace(text, "language", "programming"))
print("使用replace()函數方法2: ", text.replace("language", "programming"))

print("使用find()函數方法1: ", str.find(text, "lan"))
print("使用find()函數方法2: ", text.find("lan"))

print("使用count()函數方法1: ", str.count(text, "a"))
print("使用count()函數方法2: ", text.count("a"))

