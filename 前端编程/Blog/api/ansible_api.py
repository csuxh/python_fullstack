#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/16 17:01
import os
from django.shortcuts import render, HttpResponse, redirect


class apiDemo():
    def touch(self, request):
        os.system('touch /tmp/abc')
        return HttpResponse({'msg': '/tmp/abc has been touched'})
