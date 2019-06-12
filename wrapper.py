#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('start inner function')
        res = func(*args, **kwargs)
        print('end innter function')
        return res
    return inner

@wrapper    
def test1(name):
    print('name is: %s' %name)
    return 'call test1'
    
    
test1('xia')
print(test1.__name__)