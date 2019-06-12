#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/21 16:27
import requests

url = 'http://127.0.0.1:8000/demo2/ansible_host_api/'
data = requests.get(url)
print(data.content)