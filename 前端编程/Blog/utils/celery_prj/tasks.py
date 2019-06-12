#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/18 10:58

from __future__ import absolute_import
from .c_main import app
import time


@app.task
def add(x, y):
    time.sleep(40)
    return x + y