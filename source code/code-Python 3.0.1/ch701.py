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
        return "study a foreign language."

people = Childs()

print("繼承:", people.LangChinese())
print("繼承:", people.LangNative())
print("繼承了姓:", people.LastName)
print("屬於自己的名:", people.FirstName)
print("自己的特性, 新學習的語言", people.StudyNewLang())
