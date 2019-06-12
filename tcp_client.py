#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/6/1 9:27
#!@File : tcp_client.py

import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s.connect(('192.168.0.192', 9999))
#
# print(s.recv(1024).decode('utf-8'))
# for data in [b'nihao', b'hube', b'john', b'Sarah']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.192', 9998))
    data = input('input message: ')
    if not data:
        break
    s.send(('%s\r\n' %data).encode())
    print(s.recv(1024).decode('utf-8'))
    s.close()