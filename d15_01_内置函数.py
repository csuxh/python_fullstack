#!/usr/bin/env python
#!-*-coding:utf-8 -*-

import time

for i in range(0,101,2):
    time.sleep(0.1)
    char_num = i//2
    str = '\r %s%%: %s\n' %(i, '*' * char_num) if i == 100 else '\r %s%%: %s' %(i, '*' * char_num)
    print(str, end='', flush=True)
    
    
print(123)