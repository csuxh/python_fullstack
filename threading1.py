#!/usr/bin/env python
#!-*-coding:utf-8 -*-
import threading
from time import ctime,sleep

def loop(id, secs):
    print('loop%s start at: %s' %(id,ctime()))
    #print('start loop1 at: ', ctime())
    sleep(secs)
    print('loop%s end at: %s' %(id,ctime()))

def main():
    secs = [2,5]
    print('start threading')
    threads = []
    for i in range(len(secs)):
        th = threading.Thread(target=loop, args=(i, secs[i]))
        threads.append(th)
    
    for i in range(len(secs)):
        threads[i].start()
        
    for i in range(len(secs)):
        threads[i].join()
        
    print('end threading')
    
    
if __name__  ==  '__main__':
    main()