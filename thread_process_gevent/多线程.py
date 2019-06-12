#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/14 14:52
import threading
import time


def Traversal_5(interval):
    for i in range(5):
        print('Traversal_5:',i)
        time.sleep(interval)

def Traversal_10(interval):
    for i in range(10):
        print('Traversal_10:',i)
        time.sleep(interval)

def Traversal(job):
    print('job:{}'.format(job))
    time.sleep(1)

if __name__ == '__main__':
    t1 = int(time.time())
    threads = []
    for i in range(5):
        t = threading.Thread(target=Traversal, args=(i,))
        threads.append(t)
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    t2 = int(time.time())
    print('total_time: {}'.format(t2-t1))
    # print('start time:')
    # t1 = int(time.time())
    # tasks=[Traversal_5,Traversal_10]
    # threads = []
    # for task in tasks:
    #     t = threading.Thread(target=task,args=(1,))
    #     threads.append(t)
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # for t in threads:
    #     t.join()
    # print('end main total time:',int(time.time())-t1)