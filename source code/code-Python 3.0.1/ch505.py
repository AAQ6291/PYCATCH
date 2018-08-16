#!/usr/bin/env python
#coding=utf-8

import random

## 定義一個myrange()函數，裡面有兩個引數min與max
def myrange(min=1, max=99):
    return random.randint(min, max)

"""
呼叫函數，沒有傳入任何值，這個情況下myrange()函數會使用預設值 min=1, max=99
"""
print(myrange())

"""
呼叫函數，傳入50，雖然沒有指定50是給誰，預設順序會給min，所以min=50, max=99
"""
print(myrange(50))

"""
呼叫函數，傳入20, 30，預設順序會給min與max, 所以min=20, max=30
"""
print(myrange(20, 30))

"""
呼叫函數，只給min=80，這方式也是可以接受的。
"""
print(myrange(min=80))

"""
呼叫函數，只給max=50，這方式也是可以接受的。
"""
print(myrange(max=50))

"""
呼叫函數，max=50, min=10，雖然順序顛倒，但是因為引數有名稱，所以這方式也是可以接受的。
"""
print(myrange(max=50, min=10))


    
