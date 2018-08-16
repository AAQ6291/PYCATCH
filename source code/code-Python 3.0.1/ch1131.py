#!/usr/bin/env python
#coding=utf-8

# 載入logging模組
import logging

# 設定log file名稱及位置
log_file = "./mylog.log"

# 設定filename引數與level引數
logging.basicConfig(filename=log_file, level=logging.DEBUG)

# 寫入debug訊息
logging.debug('這是debug檔案...1')
logging.debug('這是debug檔案...12')
logging.debug('這是debug檔案...123')


