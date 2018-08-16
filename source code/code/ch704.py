#!/usr/bin/env python
#coding=utf-8

# 巢狀類別
class Group:
    def groupOwnMethod(self):
        print "in groupOwnMethod!"
    # 第2層
    class A:
        def funcA(self):
            print "in class A method funcA"
        # 第3層
        class B:
            def funcB(self):
                print "in class B method funcB"
            # 第4層
            class C:
                def funcC(self):
                    print "in class C method funcC"
                # 第5層
                class D:
                    def funcD(self):
                        print "in class D method funcD"
                    # 第6層
                    class E:
                        def funcE(self):
                            print "in class E method funcE"

                        # 第n層

# 建立instance並呼叫funcE()方法
group = Group()
group.A().B().C().D().E().funcE()

# 建立instance並呼叫funcD()方法
d = Group().A().B().C().D()
d.funcD()
