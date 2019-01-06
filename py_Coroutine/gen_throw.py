# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/07 1:41 AM
describe:
"""
def gen_func():
    try:
        yield  1
    except Exception as e:  #捕获调用发发出的异常
        print(e)
    yield 2
    yield 3
    return  "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception,"download  error")


    # 根据 gen_throw.py 与 gen_close.py 得出
    # 我们可以向生成器传入值 我们可以暂停生成器 我们可以关闭生成器  我们可以向生成器抛出异常