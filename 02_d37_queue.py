#!/usr/bin/env python
#!-*-coding:utf-8 -*-
from multiprocessing import Process,Queue

def product(q):
    q.put('produce1')
    
def consum(q):
    print(q.get())
    
    
if __name__ == '__main__':
    q = Queue()
    pro = Process(target=product, args=(q,))
    pro.start()
    consums = Process(target=consum, args=(q,))
    consums.start()

