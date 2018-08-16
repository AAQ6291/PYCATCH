#!/usr/bin/env python
#coding=utf-8

# 定義類別A
class A():
    value = 100
    def __init__(self):
        pass

    def func(self):
        return "func() in class A"

# 定義類別B, 繼承A
class B(A):
    value = 200
    def __init__(self):
        print(A.func(self))

    # 呼叫 func() 方法, 原先的func()方法被覆蓋掉.
    def func(self):
        print("Override! func() in class B")

b = B()
print(b.value)
b.func()
        
