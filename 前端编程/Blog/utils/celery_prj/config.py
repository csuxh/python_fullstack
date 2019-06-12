#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/18 10:57

from __future__ import absolute_import

CELERY_RESULT_BACKEND = 'redis://192.168.0.32:6379/5'
BROKER_URL = 'amqp://admin:admin@192.168.0.32:5672/'