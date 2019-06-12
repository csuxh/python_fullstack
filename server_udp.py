#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/6/1 9:57
#!@File : server_udp.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.0.192', 9998))

print('UDP server running on 9998')
while True:
    data, addr = s.recvfrom(1024)
    print('message from %s:%s' % addr)
    s.sendto(b'Hello, this is jack %s' %data, addr)

