#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/21 20:50
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#启动命令 celery -A Blog worker -l info

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'Blog' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
app = Celery('Blog')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))