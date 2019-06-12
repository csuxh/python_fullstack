#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/5 15:07
import sqlite3
from DBUtils.PooledDB import PooledDB
from flask_dropzone import Dropzone


class Config():
    SALT = b'ASDASQWER'
    SECRET_KEY = '12sfas2'
    # SQLITE_POOL = PooledDB(
    #     creator=sqlite3,
    #     maxcached=10,
    #     maxconnections=20,
    #     maxusage=20,
    #     database='MySqlite3.db'
    # )
    DATABASE = 'MySqlite3.db'
    dropzone = Dropzone()
    UPLOAD_PATH = '/Users/csuxh/Downloads/coding/python/python全栈/flask_project/CodeManagement/CodeManagement/upload'