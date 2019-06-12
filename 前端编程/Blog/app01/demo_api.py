#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/24 11:21
# rest framwork
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import renderers
from .models import Demo2, Ansible_Yml_Register, Ansible_Host
from .tasks import long_ansible_bg

# class Demo2ViewSet(viewsets.ModelViewSet):
from tempfile import NamedTemporaryFile
from rest_framework.decorators import  api_view
from . import tasks
from rest_framework.response import Response
import os
from celery.result import AsyncResult
from celery.worker.control import revoke
from utils import parase_hosts

@api_view(['GET', 'POST'])
def excute_long_ansible(request, format=None):
    data = request.data
    # print('#'*100)
    # print(data)
    f = NamedTemporaryFile(delete=False)
    data['log_file'] = f.name
    print('from excute_long_ansible')
    print(data)
    print(f.name)
    res = tasks.long_ansible_read_log.delay(data)
    return Response({'task_id': res.task_id, 'log_file': f.name})

@api_view(['GET', 'POST'])
def read_long_ansible(request, format=None):
    data = request.data
    print('#'*100)
    print(data.get('log_file'))
    if data.get('log_file'):
        log_file = data.get('log_file')
    else:
        log_file = '/tmp/ansible_long.log'
    print("from read_long_ansible")
    print(log_file)
    if not os.path.exists(log_file):
        data['read_flag'] = True
        data['logs'] = ''
        return Response(data)
    with open(log_file, 'r') as f:
        f.seek(data['seek'])
        data['logs'] = f.read()
        data['seek'] = f.tell()
    res = AsyncResult(data['task_id'])
    data['state'] = res.state
    if data['state'] in ['SUCCESS', 'FAILURE', 'REVOKED']:
        data['read_flag'] = False
    else:
        data['read_flag'] = True
    return Response(data)

@api_view(['GET', 'POST'])
def long_ansible_revoke(request, format=None):
    data = request.data
    task_id = data['task_id']
    print("#" * 100)
    print(task_id)
    res = AsyncResult(task_id)
    print("*" * 100)
    print(res)
    revoke(state="Sucess" ,task_id=task_id, terminate=True, signal='SIGKILL')
    return Response({'msg': task_id + ' has been revoked'})

@api_view(['GET', 'POST'])
def create_yml_file_define(request, format=None):
    req = request.data
    # obj = Ansible_Yml_Register(**request.data)
    Ansible_Yml_Register.objects.create(**req)
    return Response({'flag': True})

@api_view(['GET', 'POST'])
def delete_yml_file_define(request, format=None):
    req = request.data
    print(req)
    Ansible_Yml_Register.objects.filter(id=req['remove_id']).delete()
    # Ansible_Yml_Register.objects.create(**req)
    return Response({'flag': True})


@api_view(['GET', 'POST'])
def update_yml_file_define(request, format=None):
    data = request.data
    Ansible_Yml_Register.objects.filter(id=data['id']).update(**data)
    return Response({'flag': True})

@api_view(['GET', 'POST'])
def execute_yml_ansible(request, format=None):
    data = request.data
    f = NamedTemporaryFile(delete=False)
    data['log_file'] = f.name
    print(data)
    res = tasks.common_ansible_bg.delay(data)
    return Response({'task_id': res.task_id, 'log_file': f.name})


@api_view(['GET', 'POST'])
def create_ansible_hosts_modify(request, format=None):
    data = request.data
    Ansible_Host.objects.filter(id=data['id']).update(**data)
    flag, msg = parase_hosts.write_hosts_file()
    return Response({'msg': msg, 'flag': flag})

@api_view(['GET', 'POST'])
def create_ansible_hosts_delete(request, format=None):
    data = request.data
    Ansible_Host.objects.filter(id=data['remove_id']).delete()
    flag, msg = parase_hosts.write_hosts_file()
    return Response({'msg': msg, 'flag': flag})


#
# class Demo2ViewSet(viewsets.ModelViewSet):
#     serializer_class = modelSerializer.Demo2Serializer
#     queryset = Demo2.objects.all()
#
#     # detail必须为False , 通过url调用celery任务，返回task_id
#     @action(methods=['get', 'post'], detail=False, url_path='long_ansible_background_cmd')
#     def long_ansible_background_cmd(self, request, *args, **kwargs):
#         data = request.data#!/usr/bin/env  python
#         s1 = long_ansible_bg.delay()
#         # print(s1.task_id)
#         return Response({'task_id': s1.task_id})
#
#     #取消celery任务
#     @action(methods=['get', 'post'], detail=False, url_path='long_ansible_revoke')
#     def long_ansible_revoke(self, request, *args, **kwargs):
#         data = request.data
#         task_id = data['task_id']
#         print("#" * 100)
#         print(task_id)
#         res = AsyncResult(task_id)
#         print("*" * 100)
#         print(res)
#         revoke(state="Sucess" ,task_id=task_id, terminate=True, signal='SIGKILL')
#         return Response({'msg': task_id + ' has been revoked'})
#
#     @action(methods=['get', 'post'], detail=True, url_path='excute_long_ansible')
#     def excute_long_ansible(self, request):
#         data = request.data
#         f = NamedTemporaryFile(delete=False)
#         data['log_file'] = f.name
#         res = tasks.long_ansible_read_log.delay(data)
#         return Response({'task_id': res.task_id, 'log_file': f.name})