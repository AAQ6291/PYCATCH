#!/usr/bin/env python
#coding=utf-8

# 載入xml.dom.minidom模組
import xml.dom.minidom

# 讀取要分析的xml檔案
parser = xml.dom.minidom.parse("./question.xml")

# 初始*Mapping變數, 用來儲存比對符合的結果
subjectMapping = {}
descriptionMapping = {}
dateMapping = {}

# 使用for敘述句取出標籤為<question>
for node in parser.getElementsByTagName("question"):

   # 如果是就取出它的屬性id的值
   id = node.getAttribute("id")

   # 並同時取出<subject>, <description>與<date>標籤的資料
   subject = node.getElementsByTagName("subject")
   description = node.getElementsByTagName("description")
   date = node.getElementsByTagName("date")

   # 使用for敘述句逐筆取出<subject>內的資料
   for node1 in subject:
      # 先將暫存變數清空
      subject = ""
      # 逐筆取出childNodes內的值
      for node2 in node1.childNodes:
         if node2.nodeType == xml.dom.Node.TEXT_NODE:
            subject += node2.data

      # 將符合的資料寫入*Mapping變數
      subjectMapping[id] = subject

   # 使用for敘述句逐筆取出<description>內的資料
   for node1 in description:
      # 先將暫存變數清空
      description = ""
      # 逐筆取出childNodes內的值
      for node2 in node1.childNodes:
         if node2.nodeType == xml.dom.Node.TEXT_NODE:
            description += node2.data

      # 將符合的資料寫入*Mapping變數
      descriptionMapping[id] = description

   # 使用for敘述句逐筆取出<date>內的資料
   for node1 in date:
      # 先將暫存變數清空
      date = ""
      # 逐筆取出childNodes內的值
      for node2 in node1.childNodes:
         if node2.nodeType == xml.dom.Node.TEXT_NODE:
            date += node2.data

      # 將符合的資料寫入*Mapping變數
      dateMapping[id] = date

# 將分析後的結果輸出
print("<question id>\t\t<subject>\t\t\t\t\t<description>\t\t\t<date>")
for data in subjectMapping:
   print("%s\t\t%s\t\t\t\t\t%s\t\t\t%s" % (data, subjectMapping[data], descriptionMapping[data], dateMapping[data]))
