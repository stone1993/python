# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/07 3:38 PM
describe: python3.5 以后 有了原生的的协程 
python 为了 将语义 变得更加明确,就引入了 async 和 await 关键字 定义 原生的协程
"""




# 将函数前加上 async 标注它是协程 函数  在此函数中  await from 代替了 yield from ，async 的函数 并且 不能用 yield ,yield from

# await 后面 跟的 是 Awaitable  对象
from collections import  Awaitable

#当实现了 __await__ 它就是一个 Awaitable 对象
#
# class Awaitable(metaclass=ABCMeta):
#
#     __slots__ = ()
#
#     @abstractmethod
#     def __await__(self):
#         yield
#
#     @classmethod
#     def __subclasshook__(cls, C):
#         if cls is Awaitable:
#             return _check_methods(C, "__await__")
#         return NotImplemented

import types
@types.coroutine
def  get_loader(url):
    yield "xl__"
#   当注释掉下方 async  def  get_loader 方法 利用 上方方法
#      result = await get_loader(url)
# TypeError: object generator can't be used in 'await' expression
# 会报错 该生成器 不支持 await 方法

# 如果添加 types.coroutine 作为修饰器
# 不报错le
# 原因是 修饰器 将生成器封装 def wrapped 中最后返回
# return _GeneratorWrapper(coro) 类型
# 这个对象中 _GeneratorWrapper  重后实现了  __await__ 魔法方法   __await__ = __iter__


# async  def  get_loader(url):
#     return "xl__"

async def get_html(url):
    #do something
    result = await get_loader(url)
    return  result


if __name__ =="__main__":
    gen = get_html("www.baidu.com")

    gen.send(None)
    # 当调用原生协程 启动时调用send
    #
    #   StopIteration: xl__
    # 能获得异常的返回值

    # next(gen)
    # 当调用 next 启动 会出现错误,原生协程 只支持 send 启动
    # sys:1: RuntimeWarning: coroutine 'get_html' was never awaited