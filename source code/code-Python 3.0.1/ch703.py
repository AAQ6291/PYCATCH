#!/usr/bin/env python
#coding=utf-8

# 定義一個類別Group並在此類別內定義類別, 分別為A與B
class Group:
    def groupOwnMethod(self):
        print("in groupOwnMethod!")

    class A:
        def funcA(self):
            print("in class A method funcA")

    class B:
        def funcB(self):
            print("in class B method funcB")

# 建立instance group
group = Group()

# 呼叫Group類別內的A類別, 裡面的funcA方法
group.A().funcA()

# 我們也可以直接建立instance a
a = group.A()
a.funcA()

# 呼叫Group類別內的B類別, 裡面的funcB方法
group.B().funcB()

# 我們也可以直接建立instance b
b = group.B()
b.funcB()

