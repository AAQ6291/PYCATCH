#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 宣告user變數與passwd變數來接收使用者輸入的帳號與密碼
user = input("login:")
passwd = input("password (empty for guest):")

## 使用string.strip()函數將使用者輸入的空白字元刪除, 因為使用者可能會輸入空白字元
user = user.strip()
passwd = passwd.strip()

if (user == "" and passwd == "") or (user =="" and passwd !=""):
   print("username or password cannot be empty.")
elif user == "admin" and passwd == "!d^*^BM(;.":
   print("welcome administrator!")
elif user == "guest" and passwd == "":
   print("welcome, you're guest.")
elif user == "huang" and passwd == "12345":
   print("hello, huang!")
else:
   print("wrong username or password.")
