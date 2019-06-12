'''
import functools
def index(a1,a2):
    return a1 + a2

# 原来的调用方式
# ret = index(1,23)
# print(ret)

# 偏函数，帮助开发者自动传递参数
new_func = functools.partial(index,666)
ret = new_func(1)
print(ret)
'''

from functools import wraps
def wrap(func):
    @wraps(func)
    def call_it(*args, **kwargs):
        """wrap func: call_it"""
        print('before call')
        return func(*args, **kwargs)
    return call_it

@wrap
def hello():
    """say hello"""
    print('hello world')

from functools import update_wrapper
def wrap2(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print('before call')
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)

@wrap2
def hello2():
    """test hello"""
    print('hello world2')

if __name__ == '__main__':
    hello()
    print(hello.__name__)
    print(hello.__doc__)

    print(hello2())
    print(hello2.__name__)
    print(hello2.__doc__)

