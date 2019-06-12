#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/26 15:28
from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    @app.route('/index', methods=['post', 'get'])
    def index():
        return render_template('login.html')

    return app