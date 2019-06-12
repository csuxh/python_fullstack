#!/usr/bin/env python
#!-*-coding:utf-8 -*-
from multiprocessing import Process, Manager
import time

def main(dict):
    dict['count'] -= 1
    print('main进程： %s' %(dict['count']))

if __name__ == '__main__':
    m = Manager()
    dict = m.dict({'count':1000})
    p = Process(target=main, args=(dict, ))
    p.start()
    p.join()
    print('主进程： %s' %dict['count'])