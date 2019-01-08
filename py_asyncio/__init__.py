# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/07 5:47 PM
describe:
    asyncio 特点 
    
    包含各种特定系统的 模块化事件循环 （select poll epoll）
    传输 和 协议 抽象 
    对 TCP UDP SSL 子进程 调用以及其他的具体支持
    模仿 futures 模块 但适用于 事件循环使用的Future类
    
    基于 yield from 的协议和任务  可以用顺序的方法 编写并发的代码 
    必须产生一个 将产生阻塞IO的调用时,有接口可以将这个事件转化到线程池
    asyncio 主要用作协程 调度  实际上 也可以将多线程 多进程融合近来 
    所以 asyncio 是异步IO的库 而不仅仅是协程的库
    
    协程 需要搭配事件循环 才能最大作用
    
    模仿 threading 模块中的 同步原句 可以用在单线程的协程之间
"""