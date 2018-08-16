#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 讀取資料檔
f = file("./ch404.dat", "r")

## 逐步讀取資料檔
for line in f:

   ## 將資料進行分割並將分割後的資料寫入dats變數
   dats = line.split("||")

   ## 輸入dats序列變數裡的項目
   print(dats[0], dats[2])

## 關閉檔案
f.close()
