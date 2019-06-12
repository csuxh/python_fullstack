#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/24 12:34
import functools
def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return(ret)
    return inner

@auth
def test():
    print('test')


print(test.__name__)