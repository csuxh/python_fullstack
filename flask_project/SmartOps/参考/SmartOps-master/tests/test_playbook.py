from app.ansible2.runner import AdHocRunner, CommandRunner, PlayBookRunner, get_default_options
from app.ansible2.inventory import BaseInventory


def p():
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
    o = get_default_options(playbook_path='test1.yaml')
    p1 = PlayBookRunner(inventory=BaseInventory(hosts), options=o)
    p1.run()
    print(p1.results_callback.output)


if __name__ == '__main__':
    p()
