#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/5/29 8:50
#!@File : decorater2.py
import time

__author__ = 'jack'

def _private_1(name):
    return '_private_1'

def deco(func):
    def wrapper(*args, **kwargs):
        print('start Decorater')
        func(*args, **kwargs)
        print('from function dec')
    return wrapper

def deco2(level):
    def inner(func):
        def wrapper(*args, **kwargs):
            print(level)
            print('Start Decorater2')
            func(*args, **kwargs)
            print('End Decorater2')
        return wrapper
    return inner

@deco2(level="test")
def f1(a, b):
    print('hello from f1:')
    # time.sleep(2)
    print('The result is %d' %(a + b))

@deco2(level="test2")
def f2(a, b, c):
    print('hello from f2:')
    # time.sleep(2)
    print('The result is %d' %(a + b + c))


if __name__ ==  '__main__':
    f1(3,  4)
    f2(1, 3, 5)
    print('from decorater2')










# register = []

# def reg(func):
#     register.append(func)
#     return func
# @reg
# def f1():
#     return 3
# @reg
# def f2():
#     return 5
#
# result = []
# for id in register:
#     result.append(id)
#
# print('regester:')
# print(register)
# print('result:')
# print(result)


