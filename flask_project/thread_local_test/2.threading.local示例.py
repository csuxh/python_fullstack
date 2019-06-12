''' 示例一：
import threading
from threading import local
import time

obj = local()


def task(i):
    obj.xxxxx = i
    time.sleep(2)
    print(obj.xxxxx,i)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()
'''

"""
import threading
from threading import local

def task(i):
    print(threading.get_ident(),i)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()
"""

""" 示例二
import time
import threading
import greenlet

DIC = {}

def task(i):

    # ident = threading.get_ident()
    ident = greenlet.getcurrent()
    if ident in DIC:
        DIC[ident]['xxxxx'] = i
    else:
        DIC[ident] = {'xxxxx':i }
    time.sleep(2)

    print(DIC[ident]['xxxxx'],i)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()

"""
import time
import threading
try:
    import greenlet
    get_ident =  greenlet.getcurrent
except Exception as e:
    get_ident = threading.get_ident

class Local(object):
    def __init__(self):
        object.__setattr__(self, 'DIC', {})

    def __getattr__(self, item):
        ident = get_ident()
        if ident in self.DIC:
            return self.DIC[ident].get(item)
        return None

    def __setattr__(self, key, value):
        ident = get_ident()
        if ident in self.DIC:
            self.DIC[ident][key] = value
        else:
            self.DIC[ident] = {key:value}


obj = Local()

def task(i):
    obj.xxxxx = i
    time.sleep(2)
    print(obj.xxxxx,i)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()
