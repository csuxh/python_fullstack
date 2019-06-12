from flask import request
"""
class Foo(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def func(self):
        print(self.__age)

obj = Foo('oldboy',50)
print(obj.name)
print(obj._Foo__age)
# obj.func()
"""
class Base(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def func(self):
        print(self.__age)

class Foo(Base):
    def get_age(self):
        print(self.__age)

obj = Foo('oldboy',50)
obj.get_age()