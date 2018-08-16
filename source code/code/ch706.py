#!/usr/bin/env python
#coding=utf-8

class TaiwaneseFather:
    fLastName = '王'
    def fLangChinese(self):
        return "我會說中文."
    def fLangNative(self):
        return "也會說自己的母語."

class ForeignMother:
    mLastName = u'Lázaro'
    def mLangSpanish(self):
        return u"hable español"
    def mLangNative(self):
        return "日本語を話しなさい"

class Childs(TaiwaneseFather,ForeignMother):
    FirstName = '小明'
    def StudyNewLang(self):
        return "study a foreign language."

people = Childs()

print "(TaiwaneseFather類別)繼承:", people.fLangChinese()
print "(TaiwaneseFather類別)繼承:", people.fLangNative()
print "(TaiwaneseFather類別)繼承了姓:", people.fLastName

print "屬於自己的名:", people.FirstName
print "自己的特性, 新學習的語言", people.StudyNewLang()

print "(ForeignMother類別)繼承:", people.mLangSpanish()
print "(ForeignMother類別)繼承:", people.mLangNative()
print "(ForeignMother類別)繼承了姓:", people.mLastName

