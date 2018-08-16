#!/usr/bin/env python
# -*- coding: utf-8 -*-

import array

# 宣告a為陣列型態, 並傳入值[1,2,3,4,5]
a = array.array("i", [1,2,3,4,5])

# append()函數
a.append(6)
a.append(3)

# count()函數
print("count = ", a.count(3))

# extend()函數
a.extend([7,8,9])
print("extend([7,8,9]) = ", a)

# remove()函數
a.remove(3)
print("remove = ", a)

# reverse()函數
a.reverse()
print("reverse = ", a)


