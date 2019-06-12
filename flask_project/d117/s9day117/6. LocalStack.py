# by luffycity.com
import functools
try:
    from greenlet import getcurrent as get_ident
except:
    from threading import get_ident

class Local(object):
    __slots__ = ('__storage__', '__ident_func__')

    def __init__(self):
        # __storage__ = {1231:{'stack':[]}}
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', get_ident)

    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        # name=stack
        # value=[]
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}

    def __delattr__(self, name):
        try:
            del self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)


"""
__storage__ = {
    12312: {stack:[ctx(session/request) ,]}
}

"""

# obj = Local()
# obj.stack = []
# obj.stack.append('佳俊')
# obj.stack.append('咸鱼')
# print(obj.stack)
# print(obj.stack.pop())
# print(obj.stack)


class LocalStack(object):
    def __init__(self):
        self._local = Local()

    def push(self,value):
        rv = getattr(self._local, 'stack', None) # self._local.stack =>local.getattr
        if rv is None:
            self._local.stack = rv = [] #  self._local.stack =>local.setattr
        rv.append(value) # self._local.stack.append(666)
        return rv


    def pop(self):
        """Removes the topmost item from the stack, will return the
        old value or `None` if the stack was already empty.
        """
        stack = getattr(self._local, 'stack', None)
        if stack is None:
            return None
        elif len(stack) == 1:
            return stack[-1]
        else:
            return stack.pop()

    def top(self):
        try:
            return self._local.stack[-1]
        except (AttributeError, IndexError):
            return None



class RequestContext(object):
    def __init__(self):
        self.request = "xx"
        self.session = 'oo'



_request_ctx_stack = LocalStack()

_request_ctx_stack.push(RequestContext())


def _lookup_req_object(arg):

    ctx = _request_ctx_stack.top()

    return getattr(ctx,arg) # ctx.request / ctx.session

request = functools.partial(_lookup_req_object,'request')
session = functools.partial(_lookup_req_object,'session')


print(request())
print(session())


from flask import globals