#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/11 10:33
from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING

class d73FormsRouter(object):  # 配置d73_forms的路由，去连接mysql_db数据库
    """
    A router to control all database operations on models in the d73_forms application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read app02 models go to mysql_db DB.
        """
        if model._meta.app_label == 'd73_forms':  # app name（如果该app不存在，则无法同步成功）
            return 'mysql_db'  # hvdb为settings中配置的database节点名称，并非db name。dbname为testdjango
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write d73_forms models go to mysql_db DB.
        """
        if model._meta.app_label == 'd73_forms':
            return 'mysql_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the d73_forms app is involved.
        当 obj1 和 obj2 之间允许有关系时返回 True ，不允许时返回 False ，或者没有 意见时返回 None 。
        """
        if obj1._meta.app_label == 'd73_forms' or \
                obj2._meta.app_label == 'd73_forms':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the d73_forms app only appears in the mysql_db database.
        """
        if db == 'mysql_db':
            return model._meta.app_label == 'd73_forms'
        elif model._meta.app_label == 'd73_forms':
            return False

    def allow_syncdb(self, db, model):  # 决定 model 是否可以和 db 为别名的数据库同步
        if db == 'mysql_db' or model._meta.app_label == "d73_forms":
            return False  # we're not using syncdb on our hvdb database
        else:  # but all other models/databases are fine
            return True
        return None

# class app01Router(object):
#     """
#     A router to control all database operations on models in the
#     aew application.
#     """
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read aew models go to aew DB.
#         """
#         if model._meta.app_label == 'app01':
#             return 'default'
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write aew models go to aew DB.
#         """
#         if model._meta.app_label == 'app01':
#             return 'default'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the aew app is involved.
#         """
#         if obj1._meta.app_label == 'app01' or obj2._meta.app_label == 'app01':
#             return True
#         return None

#     def allow_migrate(self, db, model):
#         """
#         Make sure the aew app only appears in the aew database.
#         """
#         if db == 'default':
#             return model._meta.app_label == 'app01'
#         elif model._meta.app_label == 'app01':
#             return False
#         return None