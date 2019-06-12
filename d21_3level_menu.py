#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia

menu = {
    '教师': {
        '一班': {
            '语文':{},
            '数学':{
                '课代表':{},
                '学习委员':{}
            }
        },
        '二班': {
            '语文':{},
            '数学':{
                '课代表':{},
                '学习委员':{}
            }
        }
    
    },
    '学生': {
        '一班': {
            '语文':{},
            '数学':{
                '课代表':{},
                '学习委员':{}
            }
        },
        '二班': {
            '语文':{},
            '数学':{
                '课代表':{},
                '学习委员':{}
            }
        }
    
    },
    '管理员': {
        '一班': {
            '语文':{},
            '数学':{
                '课代表':{},
                '学习委员':{}
            }
        },
        '二班': {
            '语文':{},
            '数学':{
                '课代表':{},
                '学习委员':{}
            }
        }
    
    }   
}


L = [menu]
#print(L)
while L:
    for key in L[-1]:
        print(key)
    k = input('select>>').strip()
    #print(L[-1][k])
    if k in L[-1].keys() and L[-1][k]:
        L.append(L[-1][k])
    elif k == 'b':
        L.pop()
    elif k == 'q':
        break
    else:
        continue

