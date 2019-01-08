# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/08 8:14 PM
describe:
事件循环+回调(驱动生成器)+ epoll(IO多路复用)
asyncio 是 python 用于解决 异步 IO编程的一整套 解决方案
torando gevent teisted （scrapy django channnels)
torando(自己实现了 web服务器) ,django+flask(部署需要uwsgi nginx)
tornado 可以独立部署,nginx +tornado


用协程 做数据库驱动 网络驱动 一定要调用相应的 异步 仓 ，
"""

import asyncio
import time

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()   #事件循环 就像心脏 不断循环 调用相应函数

    #用法1 调用单个协程
    #loop.run_until_complete(get_html("http:www.baidu.com"))
    #
    # #用法2    调用多个协程
    # task = [get_html("www.baidu.com") for i in range(100)]
    # loop.run_until_complete(asyncio.wait(task))
    # print("use time is {}".format(time.time()- start))