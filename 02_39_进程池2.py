#!/usr/bin/env python
#!-*-coding:utf-8 -*-
from multiprocessing import  Process, Pool
import time
import os

def func(n):
    print('start func %s: %s' %(n,os.getpid()))
    time.sleep(1)
    print('end func %s: %s' % (n, os.getpid()))

if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func, args=(i,))
    pool.close()  #结束进程池接收任务
    pool.join()   #感知进程池中的任务执行结束
