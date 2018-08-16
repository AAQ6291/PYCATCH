#!/usr/bin/env python
#coding=utf-8

x = 60
y = -60
 
def absolute_value(n):
    if n < 0:
        n = -n
    return n
 
if absolute_value(x) == absolute_value(y):
    print "The absolute values of", x, "and", y, "are equal"
else:
    print "The absolute values of", x, "and", y, "are different"
