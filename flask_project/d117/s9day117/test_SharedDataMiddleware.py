#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/2 11:34
import os
from flask import Flask
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__)

app = SharedDataMiddleware(app, {
    '/shared': os.path.join(os.path.dirname(__file__), '.idea')
})

print(os.path.join(os.path.dirname(__file__), '.idea'))


if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, app)

