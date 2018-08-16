#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 載入hmac模組
import hmac, string

msg = """
This module implements the HMAC algorithm as described by RFC 2104
"""

# 建立hmac的instance, 並傳入key值與要雜湊的訊息
h = hmac.new(key="1234567890", msg=msg)

# 以16進位輸出內容
print h.hexdigest()

# 以non-ASCII輸出內容
print h.digest()

# 添加雜湊的訊息
h.update(string.letters)

# 以16進位輸出內容
a = h.hexdigest()

# 輸出
print a

# 建立另一個hmac並且傳入的key值與訊息都是一樣
i = hmac.new(key="1234567890", msg=msg+string.letters)

# 以16進位輸出內容
b = i.hexdigest()

# 輸出
print b

# 比較a與b經過雜湊後的內容是否一樣.
print "a == b", a == b
