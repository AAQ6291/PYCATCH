#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入ConfigParser模組
import configparser

# 建立config instance
config = configparser.ConfigParser()

# 讀取ini檔
config.read("./my-large.ini")

"""
使用set(section, option, value)函數去修改ini檔裡面的內容:
section是指section名稱
option是指參數的名稱
value是指參數值
"""
config.set("mysqld", "key_buffer", "128M")
config.set("client", "port", "3636")
config.set("mysqldump", "max_allowed_packet", "64M")

# 新增一個section, 並加入一個參數名稱abc = 123
config.add_section("new")
config.set("new", "abc", "123")
           
# 使用open()函數去讀取ini檔, 參數設定為 "r+"
config_file = open("./my-large.ini", "r+")

# 將ini檔寫入, 這個動作會修改先前我們設定的內容.
config.write(config_file)

# 關閉ini檔
config_file.close()
