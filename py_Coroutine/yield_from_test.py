# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/07 1:56 AM
describe:
"""
from itertools import  chain


if __name__ == "__main__1":
    a = [1,23,4]
    b = {"as":'12',"11":"22"}
    for x in chain(a,b,range(5)):
        print(x)

    # 自己实现 chain
    def my_chain(*args,**kwargs):
        for iter in args:
            yield from iter #yield from 可以简写 下面两句
            # for value in iter:
            #     yield value


        for x in my_chain(a,b):
            print(x)


if __name__ =="__main__2":
    def g1(iterable):
        yield iterable

    def g2(iterable):
        yield from iterable

    for value in g1(range(5)):
        print(value)

    for value in g2(range(5)):
        print(value)

    # 返回值
    # range(0, 5)
    # 0
    # 1
    # 2
    # 3
    # 4

if __name__ == "__main__":
    def g1(gen):
        yield from gen
    def main():
        g = g1()
        g.send(None)

        # main 调用方 g1 委托生成器 gen 子生成器
        # yield from 会在调用方（main） 和 子生成器之间产生双向通道
        # 子生成器 yield 值  因为yield fron 会直接交给main
        # main 函数 send 发送值 因为有了yield from  直接发送给 子生成器