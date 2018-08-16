#!/usr/bin/env python
#coding=utf-8

"""
# 多載overloading觀念, 註解的這個區塊無法在Python裡正常運作.
class Obj:
    def __init__(self):
        pass

    def func(self, x=0):
        print "func: x = %d ", x

    def func(self, x=0, y=x+x):
        print "func: x = %d, y = %d", x, y

    def func(self, y=0):
        print "func: y = %d ", y

"""

"""
我們可以改變觀念, 將上面的寫法改成下面的寫法,
將要傳入的參數都設定在__init__()函數內,
透過這個函數去接收使用者傳進來的值
"""
class Obj:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.printState()

    def printState(self):
        print "func: x = %d, y = %d", self.x, self.y

# class overloading.
obj1 = Obj(10)
obj2 = Obj(10, 10+10)
obj3 = Obj(y=30)

    


