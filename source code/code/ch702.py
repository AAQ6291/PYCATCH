#!/usr/bin/env python
#coding=utf-8

class TaiwaneseFather:
    LastName = '王'
    def LangChinese(self):
        return "我會說中文."
    def LangNative(self):
        return "也會說自己的母語."

class Childs(TaiwaneseFather):
    FirstName = '小明'
    def StudyNewLang(self):
        # 在子類別裡使用父類別的方法
        print "姓氏",TaiwaneseFather.LastName
        print TaiwaneseFather.LangChinese(self)
        print TaiwaneseFather.LangNative(self)
        return "study a foreign language."
    
people = Childs()
print "自己的特性, 新學習的語言", people.StudyNewLang()
