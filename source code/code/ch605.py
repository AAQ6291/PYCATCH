#!/usr/bin/env python
#coding=utf-8

# 定義一個類別, 名稱為A
class A:
    # 定義一個方法成員, 名稱為sort
    def sort(self):
        pass

# 建立一個實例(instance)
a = A()

# 呼叫方法成員a.sort()
print a.sort()

"""
在執行期間遇到x序列, 我們想要對這個序列排序,
但是在我們所定義的類別A裡面的sort()方法函數
裡面並沒有定義任何程式.
"""
x = [5,2,3,1,4]

"""
接著我們知道在python本身有一個內置的函數稱為 sorted()
這個函數是在做排序的, 所以我們決定學習它.
"""
a.sort = sorted

"""
接著重新嘗試呼叫a.sort(), 我們發現原本的sort學習了sorted()的功能
"""
print a.sort(x)

"""
另外, 我們發現所定義的類別A並沒有總合運算的功能,
但是我們知道在Python本身也有一個內置的sum()函數,
但是我們之前定義的類別A裡面沒有sum這個名稱, 可以學習嗎?
答案是可以的.
"""
a.sum = sum

"""
學習sum()函數後我們進行呼叫
"""
print a.sum(x)


