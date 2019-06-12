#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/18 11:21
from __future__ import absolute_import, unicode_literals
from .celery_config import app
from celery.schedules import crontab

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # 每10s调用 test('hello')
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # 每20s调用 test('world')
    sender.add_periodic_task(20.0, test.s('world'), expires=10)

    # 每周一早上7:30 执行 test('Happy Mondays!')
    sender.add_periodic_task(
        # crontab(hour=7, minute=30, day_of_week=1), # 可灵活修改
        crontab(1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)


if __name__ == '__main__':
    print("test")