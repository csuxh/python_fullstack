#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/18 11:20
from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('celery_periodic',
             broker='amqp://admin:admin@192.168.0.32:5672/',
             backend='redis://192.168.0.32:6379/5',
             include=['celery_periodic.periodic_task',])

app.conf.update(
    result_expires=3600,
)


# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'project.tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()