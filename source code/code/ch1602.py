# -*- coding: cp950 -*-

# 載入array類別
from jarray import array

# 宣告Java陣列型態, 'i'代表整數
a = array([0,1,2,3,4,5,6,7,8,9], 'i')

# 輸出a的型態
print "type a = %s" % (type(a))

# 使用for敘述句逐步輸出陣列a裡面的值
for x in a:
   print x
