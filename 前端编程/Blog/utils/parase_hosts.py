#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/16 22:20
#!/usr/bin/env  python
# -*- coding: utf-8 -*-

import json
import configparser
import itertools
from app01 import models

class KconfigParser(configparser.RawConfigParser):
    def write(self, fp):
        """解决ConfigParser的冒号被自动保存为等号而引起的后续解析问题"""
        if self._defaults:
            fp.write("[%s]\n" % DEFAULTSECT)
            for (key, value) in self._defaults.items():
                fp.write("%s: %s\n" % (key, str(value).replace('\n', '\n\t')))
            fp.write("\n")
        for section in self._sections:
            fp.write("[%s]\n" % section)
            for (key, value) in self._sections[section].items():
                if key != "__name__":
                    fp.write("%s: %s\n" %
                             (key, str(value).replace('\n', '\n\t')))
            fp.write("\n")

class Generate_ansible_hosts(object):
    def __init__(self, host_file):
        self.config = KconfigParser(allow_no_value=True)
        self.host_file = host_file

    def create_all_servers(self, items):
        for i in items:
            group = i['group']
            self.config.add_section(group)
            for j in i['items']:
                name = j['name']
                ssh_port = j['ssh_port']
                ssh_host = j['ssh_host']
                ssh_user = j['ssh_user']
                build = "ansible_ssh_port={0} ansible_ssh_host={1} ansible_ssh_user={2}".format(
                        ssh_port, ssh_host, ssh_user)
                self.config.set(group, name, build)
        #这里要读成str，不能用wb
        with open(self.host_file, 'w') as configfile:
            self.config.write(configfile)
        return True

def write_hosts_file():
    data = models.Ansible_Host.objects.all().values()
    generate_hosts = Generate_ansible_hosts('/tmp/hosts')
    s_data = [{'group': group, 'items': list(items)} for group, items in itertools.groupby(data, lambda x: x['group'])]
    try:
        generate_hosts.create_all_servers(s_data)
        msg = 'hosts has been create'
        flag = True
    except:
        msg = 'hosts has not been create'
        flag = False
    return flag, msg

if __name__ == '__main__':
    generate_hosts = Generate_ansible_hosts('/tmp/hosts')
    data = [
	    {
		"group": "test-group1",
		"items": [
		    {
			"name": "test1",
			"ssh_host": "127.0.0.1",
			"ssh_port": 22,
			"ssh_user": "deploy"
		    },
		    {
			"name": "test2",
			"ssh_host": "127.0.0.1",
			"ssh_port": 22,
			"ssh_user": "deploy"
		    }
		]
	    },
	    {
		"group": "test-group2",
		"items": [
		    {
			"name": "test3",
			"ssh_host": "127.0.0.1",
			"ssh_port": 22,
			"ssh_user": "deploy"
		    }
		]
	    }
	]
    generate_hosts.create_all_servers(data)