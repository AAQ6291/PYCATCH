#!/usr/bin/env python
#coding=utf-8

class lists:
    # 類別變數
    class_variable = []
    def __init__(self):
        # self.keywords 是實例變數
        self.instance_variable = []
# 建立instance a與b
a = lists()
b = lists()

# 給類別變數值
a.class_variable.extend([1,2,3,4,5])

# 呼叫instance a與b
print("call a", a.class_variable)
print("call b", b.class_variable)

# 建立instance c與d
c = lists()
d = lists()

# 給實例變數值
c.instance_variable.extend(["a","b","c","d","e"])

# 呼叫instance c與d
print("call c", c.instance_variable)
print("call d", d.instance_variable)





