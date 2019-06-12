#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/6/1 9:57
#!@File : client_udp.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'nihao', b'hube', b'john', b'Sarah']:
    s.sendto(data,('192.168.0.192', 9998))
    print(s.recv(1024).decode('utf-8'))

s.close()