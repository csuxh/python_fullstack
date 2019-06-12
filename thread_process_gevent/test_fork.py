#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/2/27 13:34
import os
import time

res = os.fork()
print('res == %d'%res)
if res == 0:
    print('我是子进程,我的pid是:%d,我的父进程id是:%d'%(os.getpid(),os.getppid()))
else:
    print('我是父进程,我的pid是:%d'%os.getpid())


# fork()运行时，会有2个返回值，返回值为大于0时，此进程为父进程，且返回的数字为子进程的PID；当返回值为0时，此进程为子进程。
# 注意：父进程结束时，子进程并不会随父进程立刻结束。同样，父进程不会等待子进程执行完。
# 注意：os.fork()无法在windows上运行。