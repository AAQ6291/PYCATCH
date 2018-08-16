#!/usr/bin/env python
# -*- coding: utf-8 -*-

import array

# 宣告a為陣列型態, 並傳入值[1,2,3,4,5]
a = array.array("i", [1,2,3,4,5])

# 宣告b為序列型態, 並傳入值[1,2,3,4,5]
b = [1,2,3,4,5]

# 查看a是否等於b, 回傳False
print("a == b ? %s " % (a == b))

# 查看a的型態
print("type of a %s" % (type(a)))

# 查看b的型態
print("type of b %s" % (type(b)))
