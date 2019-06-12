#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/5 13:34
import web
import datetime
import pymysql
pymysql.install_as_MySQLdb()

# 数据库连接
db = web.database(dbn = 'mysql', host = '192.168.0.32', db = 'apexsha', user = 'root', pw = 'xiahang')
# 获取所有文章


def get_posts():
    return db.select('entries', order='id DESC')


# 获取文章内容
def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

# 新建文章
def new_post(title, text):
    db.insert('entries',
              title=title,
              content=text,
              posted_on=datetime.datetime.utcnow())

# 删除文章
def del_post(id):
    db.delete('entries', where='id = $id', vars=locals())


# 修改文章
def update_post(id, title, text):
    db.update('entries',
              where='id = $id',
              vars=locals(),
              title=title,
              content=text)


if __name__ == '__main__':
    # new_post('apexglobe', '货代排名')
    print(get_post(1))