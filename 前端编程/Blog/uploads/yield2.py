#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia

def read_file(file_name):
    f = open(file_name, encoding = 'gb2312')
    while True:
        line = f.readline()
        if line.strip():
            yield line.strip()
            #print(line)
 
text = read_file('地址信息.sql')

for i in text:
    print(i)