#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/5 15:06
from flask import Blueprint, render_template, session, redirect, request
from ..utils import dbhelper
import os
from settings import Config

bl_index = Blueprint('index', __name__)

@bl_index.before_request
def auth():
    if not session.get('user_info'):
        return redirect('/login')
    return None

@bl_index.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@bl_index.route('/index')
def index():

    return render_template('index.html')


@bl_index.route('/user_list')
def user_list():
    user_list = dbhelper.fetchAll('select user_id, user_code, user_name from s_user', [])
    print(user_list)
    return render_template('user_list.html', user_list=user_list)

@bl_index.route('/upload_code', methods=['POST', 'GET'])
def upload():
    # user_list = dbhelper.fetchAll('select user_id, user_code, user_name from s_user', [])
    # print(user_list)
    if request.method == 'GET':
        return render_template('upload.html')
    fileobj = request.files.get('file')
    # print(fileobj)

    file_ext = fileobj.filename.rsplit('.', maxsplit=1)
    if len(file_ext) != 2 or file_ext[1] != 'zip':
        return '请上传ZIP文件', 400
    # filename = os.path.join(Config.UPLOAD_PATH, fileobj.filename)
    # fileobj.save(filename)

    # 解压
    import shutil
    import uuid
    target_path = os.path.join(Config.UPLOAD_PATH, str(uuid.uuid4()))
    shutil._unpack_zipfile(fileobj.stream, target_path)

    # 遍历文件
    total_num = 0
    total_file = 0
    for base_path, folder_list, file_list in os.walk(target_path):
        for file_name in file_list:
            file_num = 0
            file_path = os.path.join(base_path, file_name)
            # print(file_path)
            file_ext = file_name.rsplit('.', maxsplit=1)
            if len(file_ext) == 2 and file_ext[1] == 'vue':
                with open(file_path, 'rb') as f:
                    for line in f:
                        if line.strip() and not line.strip().startswith(b'#'):
                            file_num += 1
            total_num += file_num
            total_file += 1

    import datetime
    now = datetime.datetime.today()
    dbhelper.iud("insert into s_records(user_id, lines, ctime, files) values(?, ?, ?, ?)", (session['user_info']['id'], total_num, now, total_file))
    return 'upload success', 200





# @bl_index.route('/<xxx>')
# def allpages(xxx):
#     return render_template('{}.html'.format(xxx))