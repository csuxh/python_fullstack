#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/11 14:34
from DBUtils.PersistentDB import PersistentDB
import pymysql

# class dbPool():
#     __init__(self,):
#         pass


PooL = PersistentDB(
    creator = pymysql,  #使用链接数据库的模块
    maxusage = None, #一个链接最多被使用的次数，None表示无限制
    setsession = [], #开始会话前执行的命令
    ping = 0, #ping MySQL服务端,检查服务是否可用
    closeable = False, #conn.close()实际上被忽略，供下次使用，直到线程关闭，自动关闭链接，而等于True时，conn.close()真的被关闭
    threadlocal = None, # 本线程独享值的对象，用于保存链接对象
    host = '192.168.0.32',
    port = 3306,
    user = 'root',
    password = 'xiahang',
    database = 'apex_ca',
    charset = 'utf8'
)
def select_db(sql):
    conn = PooL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

