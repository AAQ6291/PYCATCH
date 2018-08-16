#!/usr/bin/env python
#coding=utf-8

# 定義operator類別
class operator:
    def __init__(self, x=None):
        operator.x = x
        operator.total = 100
    
    # 這個函數會將self.total變數遞增
    def plus(self):
        operator.total += operator.x
        return "increase,", operator.total
    
    # 這個函數會將self.total變數遞增
    def reduce(self):
        operator.total -= operator.x
        return "decrease, ", operator.total

# 建立Instance, 傳入2表示一次遞增2或遞減2
n = operator(2)
print(n.plus())
print(n.reduce())
print(n.reduce())
print(n.reduce())
