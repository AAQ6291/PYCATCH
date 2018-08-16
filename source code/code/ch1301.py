#!/usr/bin/env python
#coding=utf-8

# 載入xml.sax與xml.sax.handler模組
import xml.sax
import xml.sax.handler

# 定義XMLHandler類別並繼承xml.sax.handler.ContentHandler
class XMLHandler(xml.sax.handler.ContentHandler):
   def __init__(self):
      """
      初始化參數值, *Mapping字典變數是用來儲存比對到的資料
      subject, description與date變數是在比對時標示用,
      當找到標籤名稱該標籤就設1, 結束標籤就設0
      """
      self.subject = 0
      self.subjectMapping = {}

      self.description = 0
      self.descriptionMapping = {}

      self.date = 0
      self.dateMapping = {}

   """
   覆載 ContentHandler.startElement(),
   attrs["id"]是取出<question id="*">的值,
   初始tmp,tmp1,tmp2變數,這些變數是用來儲存標籤各自的值
   """
   def startElement(self, name, attrs):
      if name == "question":   
         self.id = attrs["id"]
      elif name == "subject":
         self.subject = 1
         self.tmp = ""
      elif name == "description":
         self.description = 1
         self.tmp1 = ""
      elif name == "date":
         self.date = 1
         self.tmp2 = ""

   """
   覆載 ContentHandler.characters(),
   當找到相對的標籤後就將值寫入各自的tmp,tmp1,tmp2變數.
   """
   def characters(self, data):
      if self.subject:
         self.tmp += data
         
      if self.description:
         self.tmp1 += data
         
      if self.date:
         self.tmp2 += data

   """
   覆載 ContentHandler.endElement(),
   當結束標籤後就將各自的變數歸0, 並將找到的值儲存在*Mapping變數內.
   """
   def endElement(self, name):
      if name == "subject":
         self.subject = 0
         self.subjectMapping[self.id] = self.tmp
         
      if name == "description":
         self.description = 0
         self.descriptionMapping[self.id] = self.tmp1
         
      if name == "date":
         self.date = 0
         self.dateMapping[self.id] = self.tmp2

# 建立 instance
parser = xml.sax.make_parser()

# 建立 handler instance
handler = XMLHandler()

# setContentHandler傳入handler實例, 表示分析語法時要參考XMLHandler()類別
parser.setContentHandler(handler)

# 讀取要分析的XML檔案
parser.parse('./question.xml')

# 將分析後的結果輸出
print("<question id>\t\t<subject>\t\t\t\t\t<description>\t\t\t<date>")
for data in handler.subjectMapping:
   print("%s\t\t%s\t\t\t\t\t%s\t\t\t%s" % (data, handler.subjectMapping[data], handler.descriptionMapping[data], handler.dateMapping[data]))

