#!/usr/bin/env  python
# -*- coding: utf-8 -*-
from celery import task
from billiard.exceptions import Terminated
import subprocess as commands
import os
import time
home_dir = os.path.abspath('.') + '/'
root_path = os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir))
ansible_dir = os.path.join(root_path, 'Blog/utils/ansible_playbook/')

def long_ansible_common(yml_file, log_file=''):
    ansible_playbook = 'utils/ansible_playbook/{0}'.format(yml_file)
    print(ansible_playbook)
    if not log_file:
    	bits = "set -o pipefail;ansible-playbook {0}|tee -a /tmp/ansible_long.log".format(ansible_playbook)
    else:
        bits = "set -o pipefail;ansible-playbook {0}|tee -a {1}".format(ansible_playbook, log_file)
    (status, output) = commands.getstatusoutput('bash -c "{0}"'.format(bits))


#测试后台任务
@task(throws=(Terminated,))
def long_ansible_bg():
    # long_ansible_common('long_cmd_1.yml')
    long_ansible_common('long_cmd_2.yml')
    return {'msg': 'long ansible cmd has been executed'}


#模拟读取实时日志
@task(throws=(Terminated,))
def long_ansible_read_log(data):
    print('start job')
    for i in range(10):
        print(str(i) + ': {0}'.format(data['yml_file']))
        long_ansible_common(data['yml_file'], data['log_file'])
    return {'msg': 'long ansible cmd has been executed'}


@task(throws=(Terminated,))
def common_ansible_bg(data):
    print('#'*100)
    print(data)
    print(type(data['operate']), data['operate'])
    # extra_vars = str(data['operate']).replace("u'", '\\"').replace("'", '\\"')
    extra_vars = data['operate']
    ansible_playbook = ansible_dir + "{0}".format(data['yml_file'])
    print("yml file: {}".format(ansible_playbook))
    bits =  "ansible-playbook {0} -e '{1}'|tee -a {2}".format(ansible_playbook, extra_vars, data['log_file'])
    comm = 'bash -c "' + 'set -o pipefail;{0}"'.format(bits)
    print("excute command: {}".format(comm))
    (status, output) = commands.getstatusoutput(comm)
    if status != 0:
        return {'flag': False}
    return {'flag': True}



@task()
def add(x, y):
    return x + y


@task
def run_test_suit(ts_id):
    print("++++++++++++++++++++++++++++++++++++")
    print('jobs[ts_id=%s] running....' % ts_id)
    time.sleep(10.0)
    print('jobs[ts_id=%s] done' % ts_id)
    result = True
    return result