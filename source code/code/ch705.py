#!/usr/bin/env python
#coding=utf-8

# 定義一個類別 Group
class Group:
    group = 10
    def __init__(self):
        pass
    def groupOwnMethod(self):
        print "in groupOwnMethod!"

# 定義一個類別 A
class A:
    def __init__(self):
        pass
    def funcA(self):
        print "in class A method funcA"

    # 巢狀類別B, 繼承Group類別
    class B(Group):
        b = 20
        def __init__(self):
            pass
        def funcB(self):
            print "in class B method funcB"
            
        # 巢狀類別C,  繼承Group類別
        class C(Group):
            def __init__(self):
                pass
            c = 30
            def funcC(self):
                print "in class C method funcC"

# 定義 instance a
a = A()

# 呼叫類別B()裡面的funcB()方法
a.B().funcB()

# 呼叫類別B().groupOwnMethod(), groupOwnMethod()方法是繼承Group類別
a.B().groupOwnMethod()

# 呼叫類別B本身的屬性b = 20
print a.B().b

# 呼叫類別B繼承Group類別的group屬性
print a.B().group

# 呼叫類別B裡面的類別C, 屬性c
print a.B().C().c

# 因為類別c也繼承了Group類別, 所以它也可以呼叫groupOwnMethod()方法
a.B().C().groupOwnMethod()
