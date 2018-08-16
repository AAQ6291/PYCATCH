#!/usr/bin/env python
#coding=utf-8

# 定義Obj類別
class Obj:
    # 在屬性名稱前加上兩個底線表示為私有(Private)變數
    __VariableHidden = 10
    def __init__(self):
        # 在屬性名稱前加上兩個底線表示為私有(Private)變數
        self.__hiddentoo = 20

    # 定義op()方法, 並對私有(Private)變數進行運算
    def op(self):
        self.__VariableHidden += 1
        print(self.__VariableHidden)

        self.__hiddentoo += 2
        print(self.__hiddentoo)

    def __bar(self):
        print("in bar!")
        
class subObj(Obj):
    def __init__(self):
        pass

    def foo(self):
        print(Obj.__VariableHidden)

# Obj類別
obj = Obj()
obj.op()

# subObj類別
subobj = subObj()

# 底下這3行的宣告都會出現AttributeError錯誤訊息。
subobj.__bar()
subobj.op()
subobj.foo()


