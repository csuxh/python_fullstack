#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia

def generator():
    print('1111')
    yield 'aaa'
    print('2222')
    yield('bbbb')
    
func1 = generator()

print(func1.__next__())
print('next \n')
print(func1.__next__())