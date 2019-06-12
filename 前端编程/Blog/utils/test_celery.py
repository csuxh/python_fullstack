#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/18 11:07
# from celery import Celery
from celery_task import add2


if __name__ == '__main__':

    res1 = add2.delay(123, 2342)

    print(res1.result)