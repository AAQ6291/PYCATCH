#!/usr/bin/env python
#coding=utf-8

# 定義insert()函數
def insert(sql):
    print("insert sql=", sql)

# 定義delete()函數    
def delete(sql):
    print("delete sql=", sql)

# 定義update()函數
def update(sql):
    print("update sql=", sql)

# 將函數名稱加入序列, 注意! 只有名稱就好, 不用加()符號
op_tbl = [insert, delete, update]

# 先輸出op_tbl觀看結果
print(op_tbl)

# 呼叫insert()函數並傳入SQL
op_tbl[0]("INSERT INTO table_name VALUES('a','b','c');")

# 呼叫delete()函數並傳入SQL
op_tbl[1]("DELETE * FROM table_name;")

# 呼叫update()函數並傳入SQL
op_tbl[2]("UPDATE table_name SET ID='a1' WHERE ID='a';")
