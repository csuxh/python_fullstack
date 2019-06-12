#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/18 09:04

from celery import Celery
import time

app = Celery('tasks', broker='redis://192.168.0.32:6379', backend='redis://192.168.0.32:6379')

app2 = Celery('tasks', broker='amqp://admin:admin@192.168.0.32:5672/', backend='redis://192.168.0.32:6379')


@app.task
def add(x, y):
    print("running...")
    return x+y

@app.task
def add(x, y):
    print("running...")
    return x+y

@app2.task
def add2(a, b):
    print("runnint app2")
    time.sleep(40)
    return a+b

