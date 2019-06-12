#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/5/29 21:30
#!@File : class_decorater.py

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')



@Foo
def bar():
    print('bar')


bar()