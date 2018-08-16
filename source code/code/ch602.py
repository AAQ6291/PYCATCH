#!/usr/bin/env python
#coding=utf-8

# 定義operator類別
class operator:
    # 這個特殊的__init__()函數會在建立實體Instance時就會執行
    def __init__(self, x=None):
        #在這裡所宣告的attributes前面如果加上self就表示全域變數
        self.x = x
        self.total = 100
        print "run __init__()"

    # 這個函數會將self.total變數遞增
    def plus(self):
        self.total += self.x
        return self.total
    
    # 這個函數會將self.total變數遞增
    def reduce(self):
        self.total -= self.x
        return self.total

# 建立Instance, 傳入2表示一次遞增2或遞減2
n = operator(2)
print "run plus method", n.plus()
print "run reduce method", n.reduce()
print "run reduce method", n.reduce()
