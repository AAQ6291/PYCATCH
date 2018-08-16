#!/usr/bin/env python
#coding=utf-8

# 定義Obj類別
class Obj:
    def foo(self):
        print("in foo!")

class subObj(Obj):
    def foo(self):
        # 可以利用回傳錯誤訊息方式來限制拒絕繼承
        raise AttributeError("'subObj' object has no attribute 'foo'")

obj = Obj()
obj.foo()

subobj = subObj()
subobj.foo()

