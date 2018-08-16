#!/usr/bin/env python

# 開啟檔案並使用w+模式
f = open("./sample-new.txt", "w+")

for line in range(100):
   print(">> %s" % (line))

   # 寫入
   f.writelines(">> %s \n" % (str(line)))

# 關閉
f.close()
