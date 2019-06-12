from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
import os
import subprocess
import json
from utils import parase_hosts
from app01 import models, modelSerializer
import itertools
# from django.core import serializers
# import .tasks import long_ansible_bg

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get("email")
        password = request.POST.get("pwd")
        user = auth.authenticate(username=user_name, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return redirect("/index/")
    return render(request, "login.html")

@login_required
def index(request):
    cur_user = request.GET.get("username")
    return HttpResponse("index page; current user:{}".format(cur_user))


def add_user(request):
    # user = User()
    user = User.objects.create_superuser(username = "jack@qq.com", password = "123456", email = "jack@qq.com")
    user.save()
    return HttpResponse("add user:{}".format(user))

def ansible_demo(request):
    if request.method == 'GET':
        return render(request, 'ansible_test.html')


# ansible普通调用：带日志，记录命令执行，返回执行结果
def touchFile(request):
    # os.system('touch /tmp/abc')
    bits = os.system('set -o pipefail;ansible localhost -a "touch /tmp/bcf"|tee -a /tmp/ansible.log')
    # (status, output) = subprocess.getstatusoutput('bash -c "{0}"'.format(bits))
    (status, output) = subprocess.getstatusoutput(format(bits))
    if status != 0:
        return HttpResponse({'msg': '/tmp/bcf has not been touched', 'output': output})
    return HttpResponse({'msg': '/tmp/bcf has been touched', 'output': output})
    # return HttpResponse({'msg': '/tmp/bcf has been touched'})

# 执行playbook
def touchFile2(request):
    # os.system('touch /tmp/abc')
    ansible_playbook = "utils/ansible_playbook/touch_7.yml"
    bits = os.system('set -o pipefail;ansible-playbook {0} |tee -a /tmp/ansible.log'.format(ansible_playbook))
    (status, output) = subprocess.getstatusoutput('bash -c "{0}"'.format(bits))
    if status != 0:
        print(output)
        return HttpResponse({'msg': '/tmp/bcf has not been touched', 'output': output})
    return HttpResponse({'msg': '/tmp/bcf has been touched', 'output': output})

# 执行playbook,带参数  request.data不存在？
def touchFile3(request):
    # qDict = request.GET
    # print(qDict.keys(), qDict.values())
    # d_dict = dict(zip(qDict.keys(), qDict.values()))
    # print(d_dict)
    # print(request.POST)
    # print('*'*120)
    # print(json.loads(request.body))
    # filename = request.POST.get("filename")
    #
    # # print(filename, type(filename))
    # data2 = {'filename': filename}
    # data = str(data2).replace("u'", '\\"').replace("'", '\\"')
    data = json.loads(request.body)

    ansible_playbook = "utils/ansible_playbook/touch_8.yml"
    bits =  'ansible-playbook {0} -e'.format(ansible_playbook) + " '{0}' ".format(data) + '|tee -a /tmp/ansible.log'
    comm = 'bash -c "' + 'set -o pipefail;{0}"'.format(bits)
    (status, output) = subprocess.getstatusoutput(comm)
    # print('status=',status)
    # print('output:', output)
    if status != 0:
        # print('#'*100)
        # print({'msg': '{0} has not been touched'.format(data), 'output': output})
        # print('#' * 100)
        ret = {'msg': '{0} has not been touched'.format(data), 'output': output}
        return HttpResponse(json.dumps(ret))
    ret = {'msg': '{0} has been touched'.format(data["filename"]), 'output': output}
    return HttpResponse(json.dumps(ret))
    # return HttpResponse("111")

# 带参数
def ansible_demo2(request):
    if request.method == 'GET':
        return render(request, 'ansible_with_vars.html')

# json格式返回主机列表
def get_host_list(request):
    if request.method == 'GET':
        data = models.Ansible_Host.objects.all()
        # ret = serializers.serialize("json", data)
        ret = modelSerializer.HostSerializer(data, many=True)
        print('#'*100)
        # print(type(ret),ret)
        # aa = json.dumps({'msg': '12313', 'flag': '123'})
        # print(aa)
        print(ret.data)
        return HttpResponse(ret.data)
        #return JsonResponse(ret.data, safe=False)

from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET', 'POST'])
def get_host_list2(request, format=None):
    if request.method == 'GET':
        host = models.Ansible_Host.objects.all()
        serializer = modelSerializer.HostSerializer(host, many=True)
        print(host)
        return Response(serializer.data)

#rest_framwork generic class 版本
from rest_framework import viewsets

class AnsibleHostApi(viewsets.ModelViewSet):
    # print('#'*100)
    queryset = models.Ansible_Host.objects.all()
    serializer_class = modelSerializer.HostSerializer

class AnsibleYmlReg(viewsets.ModelViewSet):
    # print('#'*100)
    queryset = models.Ansible_Yml_Register.objects.all()
    serializer_class = modelSerializer.Ansible_Yml_RegisterSerializer


#根据数据库重新生成hosts文件
def create_ansible_hosts(requestt):
    flag, msg = parase_hosts.write_hosts_file()
    return HttpResponse(json.dumps({'msg': msg, 'flag': flag}))

#添加new host
def create_ansible_hosts_add(request):
    # print('#'*100)
    # print(request.body)
    data = json.loads(request.body)
    print('#' * 100)
    print(data)
    # s_data = [{'group': group, 'items': list(items)} for group, items in itertools.groupby(data, lambda x: x['group'])]
    # print('#' * 100)

    new_host = models.Ansible_Host.objects.create(**data)
    new_host.save()
    flag, msg = parase_hosts.write_hosts_file()
    return HttpResponse(json.dumps({'msg': msg, 'flag': flag}))

#读取实时日志
def demo_read_log(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/demo_read_log.html')


def demo_server_deploy(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/demo_server_deploy.html')

def demo_server_create(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/demo_server_create.html')

def demo_server_modify(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/demo_server_modify.html')

def demo_server_add(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/demo_server_add.html')

def host_list(request):
    if request.method == 'GET':
        return render(request, 'demo2/pages/host_list.html')

def demo_upload(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/demo_upload.html')


#yml配置及操作
def demo_config_center(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/demo_config_center.html')

def demo_operate_interface(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/demo_operate_interface.html')

#文件上传示例
def file_upload(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/file_upload.html')

#文件上传示例
def test3(request):
    if request.method == 'GET':
        return render(request, 'test_data.html')

# 报表系统
def report_main(request):
    if request.method == 'GET':
        return render(request, 'demo2/defines/report_main.html')

# 上传到服务器
@csrf_exempt
@api_view(['GET', 'POST'])
def upload(request):
    # print(request)
    ret = request.data
    # print(ret)
    file_name = ret.get('file')
    # print(file_name)
    with open(os.path.join("uploads/", str(file_name)), "wb") as f:
        for i in request.FILES["file"].chunks():
            f.write(i)
    # print(request.data)
    return HttpResponse("ok")

# 通过ansible往各服务器推送文件
@csrf_exempt
@api_view(['GET', 'POST'])
def deploy_files(request):
    data = request.data.get('name')
    filename = data.split(',')
    print(type(filename), filename)
    f = NamedTemporaryFile(delete=False)
    data2 = {"log_file": f.name, "yml_file":"ansible_deploy_files.yml"}
    res = tasks.long_ansible_read_log.delay(data2)
    return Response({'task_id': res.task_id, 'log_file': f.name})


# celery task测试
from .tasks import run_test_suit
from celery.result import AsyncResult
from celery.worker.control import revoke

def tasks(request):
    print('before run_test_suit')
    result = run_test_suit.delay('110')
    print('after run_test_suit')
    return HttpResponse("job is runing background~")



# rest framwork
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import renderers
from .models import Demo2
from .tasks import long_ansible_bg
# class Demo2ViewSet(viewsets.ModelViewSet):
from tempfile import NamedTemporaryFile


class Demo2ViewSet(viewsets.ModelViewSet):
    serializer_class = modelSerializer.Demo2Serializer
    queryset = Demo2.objects.all()

    # detail必须为False , 通过url调用celery任务，返回task_id
    @action(methods=['get', 'post'], detail=False, url_path='long_ansible_background_cmd')
    def long_ansible_background_cmd(self, request, *args, **kwargs):
        data = request.data#!/usr/bin/env  python
        s1 = long_ansible_bg.delay()
        # print(s1.task_id)
        return Response({'task_id': s1.task_id})

    #取消celery任务
    @action(methods=['get', 'post'], detail=False, url_path='long_ansible_revoke')
    def long_ansible_revoke(self, request, *args, **kwargs):
        data = request.data
        task_id = data['task_id']
        print("#" * 100)
        print(task_id)
        res = AsyncResult(task_id)
        print("*" * 100)
        print(res)
        revoke(state="Sucess" ,task_id=task_id, terminate=True, signal='SIGKILL')
        return Response({'msg': task_id + ' has been revoked'})

    @action(methods=['get', 'post'], detail=True, url_path='excute_long_ansible')
    def excute_long_ansible(self, request):
        data = request.data
        f = NamedTemporaryFile(delete=False)
        data['log_file'] = f.name
        res = tasks.long_ansible_read_log.delay(data)
        return Response({'task_id': res.task_id, 'log_file': f.name})

    @action(methods=['get', 'post'], detail=True, url_path='file_upload')
    def file_upload(self, request):
        all_str = request.data['para']
        all_data = json.loads(all_str)
        saved_file_name = all_data['saved_file_name']    # 保存的文件名
        saved_file_dir = os.path.dirname(saved_file_name)
        filename = request.data['file']
        file_name = str(filename)
        if not os.path.exists(saved_file_dir):               # 目录不存在时，为其创建
            os.makedirs(saved_file_dir)
        try:
            destination = open(saved_file_name, 'wb+')
            for chunk in filename.chunks():
                destination.write(chunk)
            destination.close()
            return Response({'flag': True})
        except:
            return Response({'flag': False})

    # 收不到数据？？？？？
    @action(methods=['get', 'post'], detail=False, url_path='create_yml_file_define')
    def create_yml_file_define(self, request):
        ret = request
        print('#'*100)
        print(request)
        print(request.data)
        # models.Ansible_Yml_Register.objects.create(**data)
        return Response({'flag': True})


# from rest_framework.views import APIView
# @api_view(['GET', 'POST'])
# def long_ansible_background_cmd(request, format=None):
#     print('#' * 100)
#     s1 = long_ansible_bg.delay()
#     print(s1.task_id)
#     return Response({'task_id': s1.task_id})



