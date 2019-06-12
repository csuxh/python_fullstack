#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia

def generator():
    print('aaa')
    content = yield 111
    print('bbb')
    print('content: ', content)
    yield 222   
    
    
g = generator()
re1 = g.__next__()
print('ret1 ：',re1)

re3 = g.send('from send')
print('ret3 ：',re3)

#re2 = g.__next__()
#print('ret2 ：',re2)
