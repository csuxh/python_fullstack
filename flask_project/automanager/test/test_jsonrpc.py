#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/27 20:39
from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)

jsonrpc = JSONRPC(app, '/api')

@jsonrpc.method('App.index')
def index():
    return u'Welcome to Flask JSON-RPC'

if __name__ == '__main__':
    app.run()