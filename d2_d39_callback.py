#!/bin/env python
#!***coding:utf-8***
from multiprocessing import Pool
import os
def func(n):
    print('func %s' %os.getpid())
    return n+1

def func2(n):
    print('func2 %s' %os.getpid())
    print(n)

if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func, args=(i,), callback=func2)
    pool.close()
    pool.join()