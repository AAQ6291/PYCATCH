#!/usr/bin/env python
#coding=utf-8

# 定義myFirstObj類別
class myFirstObj:
    """ 建立一個簡單的物件。
    在這裡的是物件的備註說明，跟函數一樣。
    """
    count = 100
    def func(self, name):
        return "Hello", name

# 建立instance
o = myFirstObj()

# 呼叫類別內的attribute
print(o.count)

# 呼叫類別內的method
print(o.func("s"))

# 使用type查看o.func的型態
print(type(o.func))
