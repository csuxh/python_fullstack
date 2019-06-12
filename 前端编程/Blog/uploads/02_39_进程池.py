#!/usr/bin/env python
#!-*-coding:utf-8 -*-
from multiprocessing import  Process, Pool
import time
import os

def func(n):
    print(os.getpid(), n)


if __name__ == '__main__':
    pool = Pool(5)
    start = time.time()
    pool.map(func,range(10))

    t1 = time.time() - start
    # start = time.time()
    # p_lst = []
    # for i in range(100):
    #     p = Process(target=func, args=(i,))
    #     p_lst.append(p)
    #     p.start()
    # for i in p_lst:i.join()
    # t2 = time.time() - start
    # print(t1, t2)