#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

a = 1
b = 1

for c in range(1, 12):
    print (a, end=" ")
    n = a + b
    a = b
    b = n
