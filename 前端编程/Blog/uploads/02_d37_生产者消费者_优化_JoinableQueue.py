#!/usr/bin/env python
#!-*-coding:utf-8 -*-
from multiprocessing import Process,JoinableQueue
import random
import time

def producer(name, food, q):
    for i in range(5):
        time.sleep(random.randint(2,4))
        f = '%s produced %s %s' %(name,food, i)
        print(f)
        q.put(f)
    q.join() #阻塞，直到队列数据全部处理完毕，对应task_done
    
        
def consumer(name, q):
    while True:
        if q.get() is None:
            print('所有bread都吃完了')
            break
        f = q.get()
        print('\033[31m%s消费了%s\033[0m' %(name, f))
        time.sleep(random.randint(1,2))
        q.task_done()   # count - 1 计数     
    
    
if __name__ == '__main__':
    que = JoinableQueue(10)
    prod1 = Process(target=producer, args=('jack', 'bread', que))
    prod2 = Process(target=producer, args=('john', 'bread', que))
    cons1 = Process(target=consumer, args=('Alex', que))
    cons1.daemon = True
    cons2 = Process(target=consumer, args=('Max', que))
    cons2.daemon = True
    prod1.start()
    prod2.start()
    cons1.start()
    cons2.start()
    prod1.join() #感知一个进程的结束
    prod2.join()
#   que.put(None) #p1,p2都结束之后传入判断符号
#    que.put(None) #有多少个consum就要传多少个