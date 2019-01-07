# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/07 4:30 PM
describe:  线程 进程 都是系统级别的调度 协程 是用户态 下 函数级别的调度 消耗资源最少
  由生成器 == 》 协程
  
  1 用同步的方式 编写 异步的代码 
  2 在适当的时候可以暂停函数 在适当的时候 可以启动函数
  
  生成器 也是具有状态的  可以比拟 线程状态 
  
  协程的调度 是 事件循环 + 协程模式 协程是单线程模式
  # 之前 select 是 事件循环 + 回调机制 
  
  
  #小知识 python 3。5 之前 协程 都是 根据生成器实现的 
   python 3。5之后 有了 原生协程 async await 
   #tomadao 支持 python3。2 python 3。3    tomadao利用的是 生成器 完成的 协程。 
"""
import inspect

def gen_func():
    value = yield 1
    # 1 yield 返回值给调用方 ,2 value 获取调用方 send的值
    return "xl__"

if __name__ == "__main__1":


    # inspect.getgeneratorstate() 方法 能获取 生成器状态

    gen = gen_func()
    print(inspect.getgeneratorstate(gen)) #GEN_CREATED
    next(gen)
    print(inspect.getgeneratorstate(gen)) #GEN_SUSPENDED
    try:
        next(gen)
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen)) #GEN_CLOSED



#1. 用同步的方式编写异步的代码， 在适当的时候暂停函数并在适当的时候启动函数
#2。 原本的回调函数 不方便获取之前的参数 利用协程 可以很方便的 获取之前的参数
#3  子生成器 返回异常 也会向上传递 到 生成器中 ，方便捕获异常
# 子生成器的唤醒 由 select 那种决定
# 对于耗时的操作 我们都yield 出去 执行结束 在 通过时间循环 唤醒
# 此处为 伪代码 注重流程

import selectors
import socket
def get_socket_data():
    yield "bobby"

def downloader(url):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)

    try:
        client.connect((host, 80))  # 阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    selector.register(client.fileno(), EVENT_WRITE, connected)
    source = yield from get_socket_data()
    data = source.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)

def download_html(html):
    html = yield from downloader()

if __name__ == "__main__":
    #协程的调度依然是 事件循环+协程模式 ，协程是单线程模式
    pass
