#!/usr/bin/env python
#coding=utf-8

x, y = 1, 0

print "舊的寫法"
print "-------"
try:
    result = None
    try:
       result = x / y
    except ZeroDivisionError:
       print "不能除0"
    print "結果", result
finally:
     print "無條件進入finally區塊"

print "新的寫法"
print "-------"

try:
     result = x / y
except ZeroDivisionError:
     print "不能除0"
else:
     print "結果", result
finally:
     print "無條件進入finally區塊"

    


