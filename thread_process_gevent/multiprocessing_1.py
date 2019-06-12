#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/2/27 13:46
import time
import os
from multiprocessing import Process, Pool

def testA(name):
    print("{} 函数: {}; pid: {} Parent: {}".format(time.strftime('%Y%m%d %H:%M:%S'),name, os.getpid(), os.getppid()))
    time.sleep(2)

if __name__ == '__main__':
    # 简单方式
    # print(os.getpid())
    # for i in range(5):
    #     p = Process(target = testA, args = (i, ))
    #     p.start()
    #     # p.join()  等待子进程结束再往下执行
    p = Pool(6)
    for i in range(5):
        p.apply_async(testA, args=(i, ))
    p.close()
    p.join()

'''
当不给Process指定target时，会默认调用Process类里的run()方法。这和指定target效果是一样的，只是将函数封装进类之后便于理解和调用。
'''