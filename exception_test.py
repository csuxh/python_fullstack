#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/5/31 11:37
#!@File : exception_test.py

import logging

# try:
#     print('test try exception')
#     r = 10 / int('4')
#     print('result: ', r)
# except ValueError as e:
#     print('Print Exception: ', e)
# except ZeroDivisionError as e:
#     print('print exception2: ', e)
# else:   #有报错就不执行
#     print('From else')
# finally:  #始终执行
#     print('from finally')

def f1(a):
    return 10/int(a)
def f2(a):
    return 2*f1(a)

def main():
    try:
        f1('0')
    except Exception as e:
        logging.exception(e)  #程序打印错误后会继续执行

class xh_err(ValueError):
    print("id must greater than 10 ")

def test_err(s):
    n = int(s)
    if n < 10:
        raise xh_err('invalid value: %s' %s)
    return 11/n

if __name__ ==  '__main__':
    #main()
    try:
        test_err(7)
    except ValueError as e:
        print('ttt:', e)
    print('end main')
