#!/usr/bin/env python
#coding=utf-8

class OwnException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

def foo(x):
    return bar(x) + 1.0

def bar(x):
    if x < 0:
        raise OwnException("這是自訂的錯誤處理物件")
    else:
        return 10

""" Python 2.6用法如下:
try:
    print foo(-4)
except OwnException, (instance):
    print instance.parameter
"""
""" Python 3.0用法如下: """
try:
    print(foo(-4))
except OwnException as instance:
    (instance) = instance
    print(instance.parameter)
    


