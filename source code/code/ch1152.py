#!/usr/bin/env python
#coding=cp950

# 載入time模組
import time

now = time.localtime(time.time())
print("當地時間:")
print(now)

print
now = time.localtime(time.time())[:6]
print("當地時間:")
print(now)

print
now = time.gmtime(time.time())
print("UTC時間:")
print(now)

print
now = time.gmtime(time.time())[:6]
print("UTC時間:")
print(now)
