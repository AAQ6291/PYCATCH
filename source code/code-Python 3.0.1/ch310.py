#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

## 宣告num序列變數。
num = [1, 7, 5, 3, 6, 9, 0, 2, 5, 4, 8]

## num.sort()函數是將num裡面的數字由小排到大，就是常聽到的泡沫排序法。
num.sort()

## 將序列中的第一個值傳遞給pre變數。
pre = num[0]

## 接著刪除該序列的第一個值。
del num[0]

## 用for迴圈逐筆判斷重複值。
for x in num:
    if pre == x:
        print("找到重複值 =", pre)
    ## 將比對後的值儲存在pre變數，以做下一次循環比對。
    pre = x
