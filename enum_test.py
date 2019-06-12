#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/5/31 10:54
#!@File : enum.py
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 7
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1.value)