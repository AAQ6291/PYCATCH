#!/usr/bin/env python
#coding=utf-8

# 載入mmap模組
import mmap

# 使用with敘述句開啟檔案
with open("./ch205.txt", "r+") as f:

    #memory-map檔案
    map = mmap.mmap(f.fileno(), 0)

    # 讀取一行內容
    print(map.readline().decode('utf-8'))

    # 使用切片
    print(map[:12].decode('utf-8'))

    # 讀取一行內容
    print(map.readline().decode('utf-8'))
    
    # 回到memory-map檔案一開始位置
    map.seek(0)

    # 讀取一行內容
    print(map.readline().decode('utf-8'))

    # 關閉
    map.close()
