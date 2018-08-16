#!/usr/bin/env python
#coding=utf-8

# 定義函數，並使用 *args 引數
def sum(*args):
    """
    總和函數
    """
    total = 0
    for arg in args:
        total += arg
    return total

# 呼叫函數說明
print sum.__doc__

# 傳入多個參數
print sum(1,3,5,7,9)

# 傳入多個參數
print sum(2,4,6,8,10)


