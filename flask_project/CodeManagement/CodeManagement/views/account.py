#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/5 16:28
from flask import Blueprint, request, render_template, session, redirect
from ..utils import dbhelper, ecrypt

ac = Blueprint('ac', __name__)


@ac.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    user = request.form.get('user')
    passwd = request.form.get('pass')

    pass_md5 = ecrypt.encript(passwd)
    # print(user, pass_md5)

    rs = dbhelper.fetchOne("select user_id, user_name from s_user where user_code=? and passwd=?", (user, pass_md5))
    print(rs)
    if not rs:
        return '用户名密码错误'

    session['user_info'] = {'id': rs[0], 'name': rs[1]}
    return redirect('/index')

@ac.route('/logout')
def logout():
    del session['user_info']
    return redirect('/login')