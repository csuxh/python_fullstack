#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/6 10:15
# 导入驱动
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d

# 连接数据库
connect = sqlite3.connect("../MySqlite3.db")

# 指定工厂方法
connect.row_factory = dict_factory
cursor = connect.cursor()

cursor.execute("SELECT * FROM s_user")

rows = cursor.fetchone()

print(rows)

# for row in rows:
#     print(row)

# 提交操作
connect.commit()
# 关闭游标
cursor.close()
# 关闭数据库连接
connect.close()