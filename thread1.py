#!/usr/bin/env python
#!-*-coding:utf-8 -*-
import _thread
from time import sleep, ctime

def loop1():
    print('loop1')
    print('start loop1 at: ', ctime())
    sleep(5)
    print('loop1 finished at: ', ctime())


def loop2():
    print('loop2')
    print('start loop2 at: ', ctime())
    sleep(3)
    print('loop1 finished at: ', ctime())

    
def main():
    _thread.start_new_thread(loop1,())
    _thread.start_new_thread(loop2,())
    print('end thread')
    
if __name__ == '__main__':
    main()
    while 1:
        pass