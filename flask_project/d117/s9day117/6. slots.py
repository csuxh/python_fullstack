# by luffycity.com


class Foo(object):
    __slots__ = ('name',)
    def __init__(self):
        self.name = 'alex'
        # self.age = 18


obj = Foo()
print(obj.name)
# print(obj.age)