#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/6/2 9:57
#!@File : asyncio_test.py
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello jack! (%s)' %threading.currentThread() )
    yield from asyncio.sleep(5)
    print('Hello after yield! (%s)'%threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
