from app.ansible2.runner import AdHocRunner, PlayBookRunner, get_default_options
from app.ansible2.inventory import BaseInventory
import json
from app.models import Asset, User
from flask import Blueprint
from manage import jsonrpc

mod = Blueprint('user', __name__)

jsonrpc.register_blueprint(mod)


@jsonrpc.method('ansible.run(hosts=list,tasks=list)->Object', authenticated=User.check_auth)
def ansible_run(hosts, tasks):
    # host_data = [
    #     {
    #         "hostname": "testserver",
    #         "ip": "192.168.1.121",
    #         "port": 22,
    #         "username": "shuaibo",
    #         "password": "123456",
    #     },
    # ]
    # tasks = [
    #     {"action": {"module": "setup", "args": ""}, "name": "run_cmd"},
    #     {"action": {"module": "shell", "args": "whoami"}, "name": "run_whoami"},
    # ]

    hosts = hosts
    tasks = tasks
    inventory = BaseInventory(hosts)
    runner = AdHocRunner(inventory)
    ret = runner.run(tasks, "all")
    return ret.results_raw


# @jsonrpc.method('ansible.playbook(hosts=list,playbook_path=str)->Object', authenticated=User.check_auth)
def ansible_playbook(hosts, path):
    hosts = [{
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
    inventory = BaseInventory(hosts)
    options=get_default_options(playbook_path=path)
    play=PlayBookRunner(inventory=inventory,options=options)
    play.run()
    return play.results_callback.output
