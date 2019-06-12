#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/6/1 14:52
#!@File : wsgi_client.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body =  '<h1>Hello, %s!</h1>' % (environ['PATH'][1:] or 'web')
    return [body.encode('utf-8')]