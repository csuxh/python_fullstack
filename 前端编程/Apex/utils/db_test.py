#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/11 13:35
import os
import sys

if __name__ == '__main__':
    os.environ["DJANGO_SETTINGS_MODULE"] = "Apex.settings"
    import django
    django.setup()
    from d73_forms import models

    # ret = models.UserInfo.objects.all().values()
    # print(ret)

    # usr_list = [models.BookType(name="jack{}".format(i)) for i in range(1000)]
    # for i in range(1000):
    #     usr_list.append(models.UserInfo(name='jack' + str(i)))
    # models.UserInfo.objects.bulk_create(usr_list)
    # s = models.BookType.objects.all().values_list('id','caption')
    # ss = models.BookType.objects.all().get("caption")
    #
    models.BookType.objects.using('mysql_db').create(id='33', caption="English")






