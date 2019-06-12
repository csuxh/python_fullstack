#!/usr/bin/env python
#!-*-coding:utf-8 -*-
from multiprocessing import Process,Event
import time
import random

def traffic_light(e):
    while True:
        if e.is_set():
            #print('\033[31m当前是绿灯\033[0m')
            e.clear()
            print('\033[31m红灯亮\033[0m')
        else:
            #print('\033[31m当前是红灯\033[0m')
            e.set()
            print('\033[32m绿灯亮\033[0m')
        time.sleep(2)

def cars(e, i):
    if not e.is_set():
        print('car %s waiting at the cross road' %i)
        e.wait()
    print('car %s pass' %i)
#   if e.is_set():
#       print('car %s pass  the cross road' %i)
#   else:
#       print('car %s waiting' %i)
#       e.wait()
#       print('car %s pass after waiting' %i)

if __name__ == '__main__':
    e = Event()
    t_light = Process(target=traffic_light, args = (e,))
    t_light.start()
    
    for i in range(20):
        car = Process(target=cars, args = (e, i))
        car.start()
        #time.sleep(random.randint(1,3))
        time.sleep(random.random())
    