#!/usr/bin/env python
#!-*-coding:utf-8 -*-

def print_time(threadName, delay):
    count = 0
    #print(count)
    while count < 5:
        sleep(delay)
        count += 1
        print("%s: %s" %(threadName, ctime()))
