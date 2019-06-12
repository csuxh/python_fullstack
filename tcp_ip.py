#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Auther :  jack.xia
#!@Time :  2018/6/1 9:05
#!@File : tcp_ip.py
import socket

#AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn', 80)) #建立TCP连接

#2.7写法 s.send('GET / HTTP1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024) #设置每次最多接受1K字节
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

s.close() #关闭连接

header, html = data.split(b'\r\n\r\n', 1)
print(header)

with open('sina.html', 'wb') as f:
    f.write(html)

