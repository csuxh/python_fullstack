#!/bin/env python
#!-*- coding:utf-8 -*-
import os
import sys



if __name__ == '__main__':
    os.environ["DJANGO_SETTINGS_MODULE"] = "Apex.settings"
    import django
    django.setup()
    from app01 import models

    # ret = models.UserInfo.objects.all().values()
    # print(ret)

    usr_list = [models.UserInfo(name="jack{}".format(i)) for i in range(1000)]
    # for i in range(1000):
    #     usr_list.append(models.UserInfo(name='jack' + str(i)))
    models.UserInfo.objects.bulk_create(usr_list)




