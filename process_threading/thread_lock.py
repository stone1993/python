# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 12:54 AM
describe:
"""
# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/05 4:21 PM
describe:最常见的 Lock获取锁 释放锁
acquire  获取 release 释放
 锁会影响性能
 可能会导致死锁
 
 RLock 可重入锁 在同一线程中 能够多次 获取
 
 注意 获取 释放锁的简便写法
 with lock:
    n+=1 
    
等价余
lock acquire()
n+=1
lock.release()
"""
from threading import Thread,Lock,RLock
import dis

lock = Lock()
rlock = RLock()
n = 0

def add():
    global n
    global lock
    for i in range(1000000):
        lock.acquire()
        # lock.acquire()  多次获取会导致死锁
        n+=1
        lock.release()

def desc():
    global n
    global lock
    for i in range(1000000):
        lock.acquire()
        n-=1
        lock.release()

def add1():
    global n
    global rlock
    for i in range(1000000):
        rlock.acquire()
        rlock.acquire()
        rlock.acquire() # 同一线程内多次获取 不会导致死锁
        n+=1
        rlock.release()
        rlock.release()
        rlock.release()

def desc1():
    global n
    global rlock
    for i in range(1000000):
        rlock.acquire()
        n-=1
        rlock.release()


if __name__ == "__main__1":

    t1 = Thread(target=add)
    t2 = Thread(target=desc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(n)

if __name__ == "__main__":
    t1 = Thread(target=add1)
    t2 = Thread(target=desc1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(n)


