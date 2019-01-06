# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 11:37 PM
describe:
"""
def gen_func():
    # try:
    #     yield  "www.baidu.com"
    # except GeneratorExit:
    #     #raise  StopIteration
    #     pass
    #except Exception 无法捕获 GeneratorExit ，因为 GeneratorExit 继承自 BaseException
    yield  1
    yield 2
    yield 3
    return  "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    #当调用 close  #生成器内部产生 GeneratorExit 异常
    # 并且 不管异常是否 捕获except 生成器就已经结束了
    # 如果生成器内部不捕获这个异常 异常不会向上抛 所以 不要主动去捕获此异常
    print("hello")

    # 执行结果  说明生成器关闭后 继续执行其他代码 不产生异常
    #1
    #hello