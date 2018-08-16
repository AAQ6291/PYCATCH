#!/usr/bin/env python
#coding=utf-8

class TaiwaneseFather:
    LastName = '王'
    def Lang(self):
        return "我會說中文."
    def LangNative(self):
        return "也會說自己的母語."

class ForeignMother:
    LastName = 'Lázaro'
    def Lang(self):
        return "hable español"
    def LangNative(self):
        return "日本語を話しなさい"

class Childs(ForeignMother,TaiwaneseFather):
    FirstName = '小明'
    def StudyNewLang(self):
        return "study a foreign language."

people = Childs()

print("繼承:", people.Lang())
print("繼承:", people.LangNative())
print("繼承了姓:", people.LastName)
print("屬於自己的名:", people.FirstName)
print("自己的特性, 新學習的語言", people.StudyNewLang())
