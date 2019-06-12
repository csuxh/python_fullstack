"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views, demo_api
from django.conf.urls import url, include

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'demo2_api', views.Demo2ViewSet)
router.register(r'AnsibleHostApi', views.AnsibleHostApi)
router.register(r'AnsibleYmlReg', views.AnsibleYmlReg)

urlpatterns = [
    path('admin/', admin.site.urls),

    #rest router配置
    url(r'^', include(router.urls)),


    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^add_user/$', views.add_user),
    url(r'^ansible_demo/$', views.ansible_demo2),
    url(r'^ansible_demo/touchFile/$', views.touchFile2), #不带传参
    url(r'^ansible_demo/touchFile3/$', views.touchFile3), #带传参

    url(r'^demo2/demo_server_add/$', views.demo_server_add), #web接口：添加
    url(r'^demo2/demo_server_deploy/$', views.demo_server_deploy), #web接口：展示
    url(r'^demo2/demo_server_create/$', views.demo_server_create),
    url(r'^demo2/demo_server_modify/$', views.demo_server_modify),
    url(r'^demo2/demo_config_center/$', views.demo_config_center),  #yml配置中心
    url(r'^demo2/demo_operate_interface/$', views.demo_operate_interface ),  #操作中心


    # url(r'^demo2/ansible_host_api/$', views.ansible_host_api) , #js接口：返回主机列表json格式
    # url(r'^demo2/ansible_host_api/$', views.AnsibleHostApi.as_view()),

    #主机操作
    url(r'^demo2/host_list/$', views.host_list),
    url(r'^demo2/get_host_list/$', views.get_host_list),
    url(r'^demo2/create_ansible_hosts/$', views.create_ansible_hosts), #js接口：根据数据库生成hosts文件
    url(r'^demo2/create_ansible_hosts_add/', views.create_ansible_hosts_add), #js接口：添加host并重新生成host文件
    url(r'^demo2/demo_read_log', views.demo_read_log ), # 实时读取日志
    url(r'^demo2/create_ansible_hosts_modify/', demo_api.create_ansible_hosts_modify),
    url(r'^demo2/create_ansible_hosts_delete/', demo_api.create_ansible_hosts_delete),

    url(r'demo2/demo_upload/$', views.demo_upload),
    url(r'^file_upload/$', views.file_upload),
    url(r'^file_upload/upload/$', views.upload),
    url(r'^deploy_files/$', views.deploy_files),
    url(r'^test3/$', views.test3),


    # celery task
    url(r'^tasks/$', views.tasks, name='task'),
    # url(r'^demo2/long_ansible_background_cmd/$', views.long_ansible_background_cmd)

    url(r'^execute_long_ansible/$', demo_api.excute_long_ansible ),
    url(r'^read_long_ansible/$', demo_api.read_long_ansible ),
    url(r'^long_ansible_revoke/$', demo_api.long_ansible_revoke ),


    # yml管理中心 后台调用接口
    url(r'^create_yml_file_define/$', demo_api.create_yml_file_define),
    url(r'^delete_yml_file_define/$', demo_api.delete_yml_file_define ),
    url(r'^update_yml_file_define/$', demo_api.update_yml_file_define ),
    url(r'^execute_yml_ansible/$', demo_api.execute_yml_ansible ),

    url(r'^report_main/$', views.report_main),



]
