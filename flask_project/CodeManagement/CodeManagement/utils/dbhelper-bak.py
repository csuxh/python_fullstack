#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/5 15:32
from settings import Config
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect():
    conn = Config.SQLITE_POOL.connection()
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    return conn, cursor

def close(cursor, conn):
    cursor.close()
    conn.close()

def fetchAll(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    data = cursor.fetchall()
    close(cursor, conn)
    return data

def fetchOne(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    # print(sql)
    data = cursor.fetchone()
    close(cursor, conn)
    return data

def iud(sql, args):
    conn, cursor = connect()
    rows = cursor.execute(sql, args)
    conn.commit()
    close(cursor, conn)
    return rows

if __name__ == '__main__':
    pass
