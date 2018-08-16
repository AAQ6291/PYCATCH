# -*- coding: cp950 -*-
# 載入java.util套件裡的Random類別
from java.util import Random

# 建立實例
rand = Random()

# 使用for敘述句
for x in range(10):
   # 呼叫Random.nextInt()方法
   print rand.nextInt()

