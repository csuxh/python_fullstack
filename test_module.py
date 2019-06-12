#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/5/29 21:40
#!@File : test_module.py
import decorater2

if __name__ ==  '__main__':
    print('from test_module')
    #decorater2.f1(3,  4)
    print(decorater2._private_1('test'))

    #f2(1, 3, 5)