#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/19 10:29
import os
import django
django.setup()
os.environ["DJANGO_SETTINGS_MODULE"] = "reset_framwork.settings"


from app01.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))