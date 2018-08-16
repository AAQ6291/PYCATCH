#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入ConfigParser模組
import configparser

# 建立config instance
config = configparser.ConfigParser()

config.add_section("login")

config.set("login", "user", "root")
config.set("login", "passwd", "12345")

# 使用open()函數去讀取ini檔, 參數設定為 "r+"
config_file = open("./new.ini", "w")

# 將ini檔寫入, 這個動作會修改先前我們設定的內容.
config.write(config_file)

# 關閉ini檔
config_file.close()
