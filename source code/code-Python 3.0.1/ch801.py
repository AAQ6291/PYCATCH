#!/usr/bin/env python
#coding=utf-8

def foo(x):
    return bar(x) + 1.0

def bar(x):
    if x < 0:
        #使用raise敘述句去觸發except ValuError
        raise ValueError
    else:
        return 10

try:
    print(foo(-4))
except ValueError:
    print("不接受這個值.")


    


