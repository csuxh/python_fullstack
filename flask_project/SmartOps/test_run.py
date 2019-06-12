#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/27 22:28
from app.models import User, db
from flask import Flask
from config import CONFIG
from flask_jsonrpc import JSONRPC
from app import create_app
config_name = 'development'

app = create_app(config_name)

jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True, auth_backend=User.authenticate)
app.config.from_object(CONFIG[config_name])
db.init_app(app)

if __name__ == '__main__':
    app.run()