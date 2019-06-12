#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/5/29 21:56
#!@File : object.py


class Stuf(object):
    count = 0
    __slots__ = ('name', 'id', 'position')
    def __init__(self, name, id, position):
        self.__name = name
        self.__id = id
        self.__position = position
    def print_obj(self):
        print('name: %s ;id: %d ;position %s ' %(self.__name, self.__id, self.__position))

class Account(Stuf):
    pass

class IT(Stuf):
    pass

if Stuf.count != 0:
    print('测试失败!')
else:
    bart = Stuf('Bart', 12, '2-4')
    if Stuf.count != 1:
        print('测试失败!')
        Stuf.count +=1
        print('%d' %(Stuf.count + 1) )
    else:
        lisa = Stuf('lisa', 11, '2-5')
        if Stuf.count != 2:
            print('测试失败!')
        else:
            print('Stuf:', Stuf.count)
            print('测试通过!')

#stu1 = Stuf('jack', 13, '1-2')

#stu1.print_obj()
#print(stu1.id)

#print(stu1.__name)