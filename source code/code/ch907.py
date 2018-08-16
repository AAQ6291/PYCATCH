#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入ConfigParser模組
import ConfigParser

# 建立config instance
config = ConfigParser.ConfigParser()

# 讀取ini檔
config.read("./my-large.ini")

# 刪除new section內的abc參數
config.remove_option("new", "abc")

# 刪除new section
config.remove_section("new")

# 使用open()函數去讀取ini檔, 參數設定為 "r+"
config_file = open("./my-large.ini", "r+")

# 將ini檔寫入, 這個動作會修改先前我們設定的內容.
config.write(config_file)

# 關閉ini檔
config_file.close()
