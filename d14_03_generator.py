#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#列表推导  
#s = ['AE2018%d' %i for i in range(25) if i%3 == 0 ]
s = [i*i for i in range(25) if i%3 == 0 ]

print(s)

#生成器表达式： 几乎不占内存
g = (i for i in range(10))
print(g.__next__())

