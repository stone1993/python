# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/05 4:21 PM
describe:引出全局全局互斥锁
gil 全局互斥锁 global interpreter lock
gil 导致每一刻只有一个线程在CPU上执行字节码，无法将多个线程映射到CPU上
"""
from threading import Thread
import dis

n = 0

def add():
    global n
    for i in range(1000000):
        n+=1

def desc():
    global n
    for i in range(1000000):
        n-=1


if __name__ == "__main__":

    t1 = Thread(target=add)
    t2 = Thread(target=desc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(n)


# print 不为 0
# 原因是 n(资源) 在执行过程中并不是被线程一直占用，会在执行过程中会因为全局解释锁释放，另一个线程占用，
# 详细原因解析 请看 廖雪峰官网 python==》进程与线程==》多线程章节
# 全局解释锁 释放 条件由   1。执行字节码的行数
#                 2。CPU  时间片
#                 3。遇到IO操作时 主动释放（IO操作会消耗大量时间）