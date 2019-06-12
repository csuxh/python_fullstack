#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/20 09:05
import importlib


path = 'settings.Config'
p, c = path.rsplit('.', maxsplit=1)
# print(path.rsplit('.', maxsplit=1))

m = importlib.import_module(p)
cc = getattr(m, c)
print(dir(cc))

# importlib.import_module()