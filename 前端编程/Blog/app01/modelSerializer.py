#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/19 10:50
from rest_framework import serializers
from app01.models import Ansible_Host, Demo2, Ansible_Yml_Register

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ansible_Host
        fields = ('id', 'group', 'name', 'ssh_host', 'ssh_user', 'ssh_port', 'server_type', 'comment')


class Demo2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Demo2
        fields = '__all__'

# class Ansible_Yml_RegisterSerializer2(serializers.ModelSerializer):
#
#     class Meta:
#         model = Ansible_Yml_Register2
#         fields = '__all__'

class Ansible_Yml_RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ansible_Yml_Register
        fields = ('id', 'yml_file', 'yml_maintenancer', 'yml_parameter', 'accept_host_group', 'comment', 'register_time')
