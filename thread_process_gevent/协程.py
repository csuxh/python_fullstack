#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/14 10:20
# 单线程的异步编程模型称为协程
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
import time

def Traversal(job):
    print('job:{}'.format(job))
    time.sleep(1)


if __name__ == '__main__':
    print('start running:')
    s_time = int(time.time())
    jobs = [i for i in range(10)]
    pool = Pool(5)
    pool.map(Traversal, jobs)
    print('end')
    e_time = int(time.time())
    print('total_time: {}'.format(e_time - s_time))