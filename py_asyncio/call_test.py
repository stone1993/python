# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/09 12:24 PM
describe: call_soon call_at call_later call_soon_threadsafe
"""
import asyncio

if __name__ == "__main__":
    def get_html(n_time):
        print("{} sleep".format(n_time))

    def stoploop(loop): #因为调用 run_fover 需要停止 如何停止 创建一个函数 停止事件循环  放入队列要执行的事件中
        loop.stop()

    loop = asyncio.get_event_loop()
    now = loop.time()  #时间是事件循环 内部时钟时间 与 系统时间无关

    loop.call_soon(get_html,3)  #立即执行(当等到下一轮事件循环时执行）

    #loop.call_later(2,get_html,5)  #call_later 延时时间后调用
    loop.call_at(now+2,get_html,44) #指定时间 调用
    #loop.call_soon(stoploop,loop)   #
    loop.run_forever() # 不能 run_until_complete 因为事件不是一个协程

    #call_soon_threadsafe用法和call_soon一致。但在涉及多线程时， 会使用它.

    #call_soon, call_later, call_at, call_soon_threadsafe都是比较底层的，在正常使用时很少用到。