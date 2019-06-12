#!/usr/bin/env python
#!-*-coding:utf-8 -*-
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8999))
print(sk.recv(1024).decode('utf-8'))
msg = input('input message>>>').encode('utf-8')
sk.send(msg)
sk.close()