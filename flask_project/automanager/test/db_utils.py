#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/27 20:45
from flask import Flask
from flask_jsonrpc import JSONRPC
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import werkzeug

app = Flask(__name__)

jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '1q2w3e'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(164))

    def password(self, password):
        """
        设置密码hash值
        """
        self.password_hash = werkzeug.security.generate_password_hash(password)

    def verify_password(self, password):
        """
        将用户输入的密码明文与数据库比对
        """
        return werkzeug.security.check_password_hash(password)
    def __init__(self, username, passwd):
        self.username = username
        self.password = passwd

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    db.create_all()
    # admin = User('admin', 'admin@example.com')
    # db.session.add(admin)
    # db.session.commit()