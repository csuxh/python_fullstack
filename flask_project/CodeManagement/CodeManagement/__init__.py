#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/5 15:03
from flask import Flask
from .views.index import bl_index
from .views.account import ac
from settings import Config


def my_app():
    app = Flask(__name__, static_folder='assets')
    app.config.from_object('settings.Config')

    # app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
    # app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*, .pdf, .txt, .zip'
    Config.dropzone.init_app(app)

    app.register_blueprint(bl_index, url_prefix='')
    app.register_blueprint(ac)
    return app


