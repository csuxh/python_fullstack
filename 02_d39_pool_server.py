#!/usr/bin/env python
#!-*-coding:utf-8 -*-
import socket
from multiprocessing import Pool

def func(conn):
    msg = '你好'
    conn.send(msg.encode('utf-8'))
    recv = conn.recv(1024).decode('utf-8')
    print(recv)
    conn.close()

if __name__ == '__main__':
    pool = Pool(5)
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8999))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        pool.apply_async(func, args=(conn,))
    sk.close()
