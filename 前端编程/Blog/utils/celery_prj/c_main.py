#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/18 10:57

from __future__ import absolute_import
from celery import Celery

app = Celery('celery_prj', include=['celery_prj.tasks'])

app.config_from_object('celery_prj.config')

if __name__ == '__main__':
    app.start()