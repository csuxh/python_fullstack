#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/6 20:50
import time
from queue import Queue
from settings import Config

class PoolException(Exception):
    pass


class Pool(object):
    '''''一个数据库连接池'''

    def __init__(self, maxActive=5, maxWait=None, init_size=0, db_type="SQLite3", **config):
        self.__freeConns = Queue(maxActive)
        self.maxWait = maxWait
        self.db_type = db_type
        self.config = config
        if init_size > maxActive:
            init_size = maxActive
        for i in range(init_size):
            self.free(self._create_conn(check_same_thread=False))

    def __del__(self):
        print("__del__ Pool..")
        self.release()

    def release(self):
        '''''释放资源，关闭池中的所有连接'''
        print("release Pool..")
        while self.__freeConns and not self.__freeConns.empty():
            con = self.get()
            con.release()
        self.__freeConns = None

    def _create_conn(self):
        '''''创建连接 '''
        if self.db_type in dbcs:
            return dbcs[self.db_type](**self.config);

    def get(self, timeout=None):
        '''''获取一个连接
        @param timeout:超时时间
        '''
        if timeout is None:
            timeout = self.maxWait
        conn = None
        if self.__freeConns.empty():  # 如果容器是空的，直接创建一个连接
            conn = self._create_conn()
        else:
            conn = self.__freeConns.get(timeout=timeout)
        conn.pool = self
        return conn

    def free(self, conn):
        '''''将一个连接放回池中
        @param conn: 连接对象
        '''
        conn.pool = None
        if (self.__freeConns.full()):  # 如果当前连接池已满，直接关闭连接
            conn.release()
            return
        self.__freeConns.put_nowait(conn)


from abc import ABCMeta, abstractmethod


class PoolingConnection(object, metaclass=ABCMeta):
    def __init__(self, **config):
        self.conn = None
        self.config = config
        self.pool = None

    def __del__(self):
        self.release()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def release(self):
        print("release PoolingConnection..")
        if (self.conn is not None):
            self.conn.close()
            self.conn = None
        self.pool = None

    def close(self):
        if self.pool is None:
            raise PoolException("连接已关闭")
        self.pool.free(self)

    def __getattr__(self, val):
        if self.conn is None and self.pool is not None:
            self.conn = self._create_conn(**self.config)
        if self.conn is None:
            raise PoolException("无法创建数据库连接 或连接已关闭")
        return getattr(self.conn, val)

    @abstractmethod
    def _create_conn(self, **config):
        pass


class SQLit3PoolConnection(PoolingConnection):
    def _create_conn(self, **config):
        import sqlite3
        return sqlite3.connect(**config)


dbcs = {"SQLite3": SQLit3PoolConnection}

pool = Pool(database=Config.DATABASE)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect():
    conn = pool.get()
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

if __name__ == "__main__":
    pass