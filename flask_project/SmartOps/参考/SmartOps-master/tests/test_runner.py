# -*- coding: utf-8 -*-
#

import unittest
import sys

sys.path.insert(0, "../..")

from app.ansible2.runner import AdHocRunner, CommandRunner,PlayBookRunner
from app.ansible2.inventory import BaseInventory


class TestAdHocRunner(unittest.TestCase):
    def setUp(self):
        host_data = [
            {
                "hostname": "testserver",
                "ip": "192.168.1.121",
                "port": 22,
                "username": "shuaibo",
                "password": "123456",
            },
        ]
        inventory = BaseInventory(host_data)
        self.runner = AdHocRunner(inventory)

    def test_run(self):
        tasks = [
            {"action": {"module": "shell", "args": "ls"}, "name": "run_cmd"},
            {"action": {"module": "shell", "args": "whoami"}, "name": "run_whoami"},
        ]
        ret = self.runner.run(tasks, "all")
        print(ret.results_summary)
        print(ret.results_raw)


class TestCommandRunner(unittest.TestCase):
    def setUp(self):
        host_data = [
            {
                "hostname": "testserver",
                "ip": "192.168.1.121",
                "port": 22,
                "username": "root",
                "password": "123456",
            },
        ]
        inventory = BaseInventory(host_data)
        self.runner = CommandRunner(inventory)

    def test_execute(self):
        res = self.runner.execute('ls', 'all')
        print(res.results_command)
        print(res.results_raw)
class TestPlaybookRunner(unittest.TestCase):
    pass
def p():
    hosts=[{
        "hostname": "manager2",
        "ip": "192.168.1.121",
        "port": 22,
        "username": "shuaibo",
        "password": "123456",
        "become": {
            "method": "sudo",
            "user": "root",
            "pass": None,
        },
        "groups": ["hadoop", "test"],
        "vars": {"sexy": "yes"},
    }, {
        "hostname": "ubuntu",
        "ip": "192.168.1.238",
        "port": 22,
        "username": "root",
        "password": "111111a",
        "private_key": "/tmp/private_key",
        "become": {
            "method": "su",
            "user": "root",
            "pass": "123",
        },
        "groups": ["hadoop", "test"],
        "vars": {"love": "yes"},
    }]
    p1=PlayBookRunner(inventory=hosts,playbook_path='test1.yaml')
    p1.run()
    print(p1.results_callback)


if __name__ == "__main__":
    p()
    # unittest.main()
