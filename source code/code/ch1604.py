# -*- coding: cp950 -*-

# 載入java.util與java.lang套件
from java.util import Random
from java.lang import Math

# 定義一個subclass
class myRand(Random):
    #__init__()函數就是Java的建構函數（Constructor）
    def __init__(self, multiplier=100):
        self.multiplier = multiplier

    #　覆載（Override）
    def nextInt(self):
        return Math.random() * self.multiplier

# 建立實例
r = myRand(100)

for i in range(10):
    print r.nextInt()

