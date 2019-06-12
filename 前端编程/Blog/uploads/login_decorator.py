#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
FLAG = False
def login(func):
    def inner(*args, **kwargs):
        global FLAG
        if FLAG:
            res = func(*args, **kwargs)
            return res
        else:
            username = input('Pls input username:')
            password = input('Pls input password:')
            if username == 'jackxia' and password == 'xiahang':
                print('login successful')
                FLAG = 1
                res = func(*args, **kwargs)
                return res
            else:
                print('wrong username or password')
    
    return inner

@login    
def addUser(usr, password):
    print('add user: %s, passwd: %s' %(usr,password))
    return 1

add = addUser('John', '123456')
