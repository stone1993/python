# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/11 1:00 AM
describe:
"""



import asyncio
if __name__ == "__main__1":

    n = 0
    async def add():
        global n
        for i in range(1000000):
            n += 1


    async def desc():
        global n
        for i in range(1000000):
            n -= 1

    loop = asyncio.get_event_loop()
    task = [add(),desc()]
    loop.run_until_complete(asyncio.wait(task))
    print(n)
    # 输出结果为 0
    # 原因 单线程 不需要锁 只要task内没有阻塞 会一直运行结束 再运行另一个task 所以不存在资源的竞争


# 此例子说明 为什么 协程也需要同步
if __name__ == "__main__":

    import aiohttp
    from asyncio import Lock ,Queue
    cache = {}

    look = Lock()
    queue = Queue()
    # 多线程的queue 当队列满时 存数据会阻塞 当队列为空 取数据也会阻塞
    # 协程的 queue 不会阻塞
    # 全部变量 队列 [] 也能在协程中当作消息队列使用，但不能控制 队列的大小

    async def get_stuff(url):

        # 同步 上锁 方式1 acquire release
        await look.acquire()
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET,',url)
        cache[url] = stuff
        return stuff
        await look.release()

        # 上锁 方式2

        with await look:
            #do somethong

        # 协程 上锁 方式3
        # 普通的with 上下文 实现的是 __exit__,__enter__

        # 协程的上下文 实现的是 __aexit__,__aenter__ 魔法方法
        async with look:
            # do somethong



    async def parse_stuff():
        stuff = await get_stuff()
        # do something
        # 获取url 解析

    async def use_stuff():
        stuff = await get_stuff()
        # do something
        # 获取 url 使用

# 如果 get_stuff 中 await 反应很慢的话
# 两个协程很有可能都阻塞在这里,并且调用的是用一个 url 请求。(我们的设计 是想实现 相同的url 请求 只占用一次)
# 两个相同的请求 比较耗时 而且 容易触发反爬虫机制
# 故 协助之间 也需要同步机制

tasks = [parse_stuff(),use_stuff()]
