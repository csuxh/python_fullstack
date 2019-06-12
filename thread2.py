#!/usr/bin/env python
#!-*-coding:utf-8 -*-
import _thread
from time import sleep, ctime

def print_time(threadName, delay):
    count = 0
    print(count)
    while count < 5:
        sleep(delay)
        count += 1
        print("%s: %s" %(threadName, ctime()))
        


_thread.start_new_thread( print_time,("thread1",2, ))
_thread.start_new_thread( print_time,("thread2",4, ))
print('end thread')


while 1:
    pass