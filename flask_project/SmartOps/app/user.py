#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/27 21:35
from flask import Blueprint

mod = Blueprint('user', __name__)
from manage import jsonrpc
jsonrpc.register_blueprint(mod)
from app.models import User
from app import db


@jsonrpc.method('user.register(username=str,password=str)')
def user_register(username, password):
    if not User.query.filter_by(username=username).first():
        user = User(username=username)
        user.password(password)
        db.session.add(user)
        db.session.commit()
        return {'status': 0, 'message': u'注册成功'}
    else:
        return {'status': 1, 'message': u'用户已存在'}


@jsonrpc.method('user.verify(username=str,password=str)')
def user_verify(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return {'status': 1, 'message': u'用户名不存在'}
    if user.verify_password(password):
        token = user.generate_auth_token()
        return {'status': 0, 'message': u'欢迎%s' % username, 'token': token}
    return {'status': 1, 'message': u'密码错误'}