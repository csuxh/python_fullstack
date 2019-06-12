#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia

def generator():
    print('aaa')
    yield 111
    print('bbb')
    yield 222   
    
g = generator()
re1 = g.__next__()
print(re1)

re2 = g.__next__()
print(re2)
