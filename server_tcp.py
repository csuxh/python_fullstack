#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/6/1 9:18
#!@File : server_tcp.py
import socket
import time
import threading

def tcplink(sock, addr):
    print('Accept connection from %s:%s...' %addr)
    sock.send(b'Welcome to connect to jacks computer')
    while True:
        data = sock.recv(1024)
        time.sleep(3)
        print(data)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' %data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed.' %addr )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #SOCK_STREAM指定使用面向流的TCP协议

s.bind(('192.168.0.192', 9999))
s.listen(5)
print('Waiting for connection....')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


