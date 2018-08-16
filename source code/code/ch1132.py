#!/usr/bin/env python
#coding=utf-8

# 載入logging模組
import logging
import glob
import logging.handlers

# 設定log file名稱及位置
log_file = "./mylog1.log"

# 設定logger名稱
logger = logging.getLogger("example")

# 設定等級
logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
# 使用logging.handlers.RotatingFileHandler()函數來控制紀錄檔的大小與分割的數量.
handler = logging.handlers.RotatingFileHandler(
   filename=log_file, maxBytes=500, backupCount=5)

# 設定寫入紀錄檔的格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# 傳入handler實例
logger.addHandler(handler)

# 使用for敘述句連續寫入測試log
for i in range(500):
    logger.debug('i = %d' % i)

# 列出所產生的log檔案名稱
logfiles = glob.glob('%s*' % log_file)

for filename in logfiles:
    print filename

