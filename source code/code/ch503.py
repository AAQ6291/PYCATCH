#!/usr/bin/env python
#coding=utf-8

## 宣告一個序列變數
lists = [1,2,3]

## 定義函數chage_lists() 
def chage_lists():
    ## 改變序列的值
    global lists
    lists = ["how","are","you"]

## 錯誤的使用函數方法，因為後面沒有()。
chage_lists

## 使用函數
chage_lists()

## 列印出序列的值
print lists

    
