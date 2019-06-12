#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia

def init_generator(f):
    def inner(*args, **kwargs):
        g = f(*args, **kwargs)
        g.__next__()
        return g
    return inner
    
@init_generator
def avage():
    sum = 0
    cnt = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        cnt += 1
        avg = sum/cnt


av = avage()   
av1 = av.send(10)
av2 = av.send(20)
av3 = av.send(30)

print('av1: %s , av2: %s, av3: %s' %(av1,av2,av3))