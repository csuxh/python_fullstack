#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/5/28 16:42
#!@File : decorater.py
import sys
import datetime

def log(func):
    def inner(*args, **kw):
        print('call function: %s' % func.__name__)
        return func(*args, **kw)
    print(sys.version)
    return inner()

@log
def now():
    time_stamp = datetime.datetime.now()
    print(time_stamp)


now()