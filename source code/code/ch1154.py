#!/usr/bin/env python
#coding=cp950

# 載入time模組
import time

# 定義時間
now = time.localtime(time.time())

# 將時間以字串格式輸出
print(time.asctime(now))

# 定義時間
now = time.time()

# 將時間以字串格式輸出
print(time.ctime(now))
