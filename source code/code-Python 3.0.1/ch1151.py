#!/usr/bin/env python
#coding=cp950

# 載入time模組
import time

# 設定開始時間
start_time = time.time()

# 停止2秒
time.sleep(3)

# 設定結束時間
end_time = time.time()

# 結束時間 - 開始時間 = 執行時間
print("執行時間: %s 秒" % (end_time - start_time))
