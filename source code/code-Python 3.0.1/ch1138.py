#!/usr/bin/env python
#coding=utf-8

# 載入smtplib模組
import smtplib, base64

# 指定寄件者
from_addr = "huang@python.tw"

# 指定收件者
to_addr = "python.tw@gmail.com"

# 設定主旨
subject = "測試email, 這封是用python產生的"

# 撰寫email內容
msg = """
   這是信件的內容..
"""

# email header
headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (from_addr, to_addr, subject)

# 建立instance並傳入SMTP的位置
server = smtplib.SMTP('localhost')

server.ehlo()
server.starttls()
server.ehlo()

# 登入帳號與密碼
server.docmd("AUTH LOGIN", base64.b64encode("my_name"))
server.docmd(base64.b64encode("my_password"), "")

# 使用sendmail()函數送信
server.sendmail(from_addr, to_addr, headers+msg)

# 離開
server.quit()
