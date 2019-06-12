#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/4/5 16:06
import hashlib
from settings import Config

def encript(text):
    # 调用hashlib的md5，输入参数aaa，并把aaa按utf-8编码bytes
    # 调用md5的hexdigest方法进行转化
    hash = hashlib.md5(Config.SALT)
    # hash = hashlib.md5(b'ASDASQWER')
    hash.update(bytes(text, encoding='utf-8'))
    rs = hash.hexdigest()
    return rs

if __name__ == '__main__':
    print(encript('123456'))