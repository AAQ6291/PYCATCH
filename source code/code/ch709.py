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
        print self.__VariableHidden

        self.__hiddentoo += 2
        print self.__hiddentoo

# 建立Instance
obj = Obj()

# 呼叫op()方法
obj.op()

# 嘗試呼叫私有(Private)變數
print obj.__VariableHidden
print obj.__hiddentoo
