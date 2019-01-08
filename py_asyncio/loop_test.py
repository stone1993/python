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



if __name__ == "__main__1":
    async def get_html(url):
        print("start get url")
        await asyncio.sleep(2)
        print("end get url")



    start = time.time()
    loop = asyncio.get_event_loop()   #事件循环 就像心脏 不断循环 调用相应函数

    #用法1 调用单个协程
    #loop.run_until_complete(get_html("http:www.baidu.com"))
    #
    # #用法2    调用多个协程
    # task = [get_html("www.baidu.com") for i in range(100)]
    # loop.run_until_complete(asyncio.wait(task))
    # print("use time is {}".format(time.time()- start))



# 获取 协程的返回值
if __name__ == "__main__2":
    async def get_html(url):
        print("start get url")
        await asyncio.sleep(2)
        print("end get url")
        return "xl___"


    start = time.time()
    loop = asyncio.get_event_loop()   #事件循环 就像心脏 不断循环 调用相应函数


    # 方法1 像线程那样 submit 体检程序
    # ensure_future 函数中 将协程 与 loop 做了绑定
    # 因为 一个线程只有一个 loop
    #ensure_future 函数中 get_event_loop 与主线程的loop 相同
    # 然后 就和方法2 相同 调用 create_task
    get_future = asyncio.ensure_future(get_html("www.baidu.com"))

    #run_untile_complete 可以接受的参数类型比较丰富 可接受Future类型 也可以接受 协程类型
    loop.run_until_complete(get_future)

    # 获取协程返回值
    print(get_future.result())


    #方法2
    # loop.create_task()  Task 类型其实是 Future的子类
    task = loop.create_task(get_html("www.baidu.com"))
    loop.run_until_complete(task)
    print(task.result())



# 当协程结束 触发 相应方法
if __name__ == "__main__111":
    async def get_html(url):
        print("start get url")
        await asyncio.sleep(2)
        print("end get url")
        return "xl___"

    def callback(futures):
        print(futures)
        print("----------end--------------")


    def callback2(url,futures): #带有参数的 回调函数
        print(url)
        print("----------end--------------")


    start = time.time()
    loop = asyncio.get_event_loop()   #事件循环 就像心脏 不断循环 调用相应函数



    get_future = asyncio.ensure_future(get_html("www.baidu.com"))

    #get_future.add_done_callback(callback)      #当协程结束触发
                                                # 当add_done_callback 触发的函数 需要参数 可以 用偏函数方式结束
                                                #from functools import partial
    from functools import partial
    get_future.add_done_callback(partial(callback2,"www.sohu.com"))

    #run_untile_complete 可以接受的参数类型比较丰富 可接受Future类型 也可以接受 协程类型
    loop.run_until_complete(get_future)

    #start get url
    #end get url
    #<Task finished coro=<get_html() done, defined at /Users/xl/Documents/code/git_python/py_asyncio/loop_test.py:80> result='xl___'>
    #----------end--------------
    #  futures 即 task
    # 触发结果 当协程结束 调用 callback
    #


# wait 与 gather
if __name__ == "__main__":
    async def get_html(url):
        print("start get url")
        await asyncio.sleep(2)
        print("end get url")
        return "xl___"


    start = time.time()
    loop = asyncio.get_event_loop()   #事件循环 就像心脏 不断循环 调用相应函数

    #task = [get_html("www.baidu.com") for i in range(100)]

    # asyncio.wait  具有修饰起 @coroutine 因此 他是一个协程
    # 操作类似 线程池 wait 等到线程池所有的任务结束
    # 这里操作等到 所有的协程 程序结束
    #  wait 函数 return_when 参数 也类似 线程池 wait
    #FIRST_COMPLETED = concurrent.futures.FIRST_COMPLETED  第一个完成
    #FIRST_EXCEPTION = concurrent.futures.FIRST_EXCEPTION 第一个异常
    #ALL_COMPLETED = concurrent.futures.ALL_COMPLETED     所有协程 完成
    #
    # 提交方式1 wait
    #loop.run_until_complete(asyncio.wait(task))

    #方式2 gather
    # gather 提交参数时 与wait 不同 ，需要加*号 将数组转化为一个个参数
    #loop.run_until_complete(asyncio.gather(*task))
    #print("use time is {}".format(time.time()- start))

    #gather 与 wait 的区别

    #gather 比wait 更高级
    # gather 可以将 协程 分组

    # gather的 调用方式1
    group1 = [get_html("www.baidu.com") for i in range(2)]
    group2 = [get_html("www.baidu.com") for i in range(2)]
    # loop.run_until_complete(asyncio.gather(*group1,*group2))
    # print("use time is {}".format(time.time()- start))

    # gather的调用方式2
    group1 =asyncio.gather(*group1)
    group2 =asyncio.gather(*group2)

    loop.run_until_complete(asyncio.gather(group1,group2))
    print(group2.cancel()) # 可以取消协程 取消失败 返回false
    print("use time is {}".format(time.time()- start))
