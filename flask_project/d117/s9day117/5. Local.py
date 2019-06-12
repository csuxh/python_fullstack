# by luffycity.com
"""
{
    1232:{k:v}
}


"""
try:
    from greenlet import getcurrent as get_ident
except:
    from threading import get_ident

"""
class Local(object):
    
    def __init__(self):
        object.__setattr__(self,'storage',{})
    
    def __setattr__(self, key, value):
        ident = get_ident()
        if ident not in self.storage:
            self.storage[ident] = {key:value}
        else:
            self.storage[ident][key] = value
            
    def __getattr__(self, item):
        ident = get_ident()
        if ident in self.storage:
            return self.storage[ident].get(item)
"""


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



obj = Local()
obj.stack = []
obj.stack.append('佳俊')
obj.stack.append('咸鱼')
print(obj.stack)
print(obj.stack.pop())
print(obj.stack)