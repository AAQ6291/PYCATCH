#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入ConfigParser模組
import ConfigParser

# 建立config instance
config = ConfigParser.ConfigParser()

# 讀取ini file
config.read("./my-large.ini")

"""
設定讀取mysqld section裡面的所有參數名稱,
注意, 這裡只會回傳section名稱, 例如：

key_buffer

而不是一整行:

key_buffer = 256M

完整的options內容為：

['query_cache_size',
'key_buffer',
'socket',
'sort_buffer_size',
'read_rnd_buffer_size',
'myisam_sort_buffer_size',
'table_cache',
'thread_concurrency',
'max_allowed_packet',
'thread_cache_size',
'port',
'read_buffer_size']
"""
options = config.options("mysqld")

# 接著利用get()函數去讀取該參數的值
for option in options:
   print option, "=", config.get("mysqld", option)
