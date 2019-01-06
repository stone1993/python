# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 11:00 PM
describe: 由C10M 问题  如何利用8核心CPU,64G内存,在10gbps 的网络上保持10000万并发连接
引入协程

1. 回调模式 编码复杂度高
2. 同步编码的复杂性不高
3. 多线程 编程 需要线程间同步 lock

1. 采用同步的方式去编写 异步的代码
2. 不在需要锁 并发性高 如果单线程内切换函数 性能高于线程切换,并发性更高。
"""
def get_url(url):
    #do something
    html = get_html(url) #此处暂停,切换到另一个函数中去执行
    # parse html
    urls = parse_url(html)

# 传统函数调用 A>B>C
# 我们需要一个可以暂停的函数,并且在适当的时候可以恢复盖函数的继续执行
# 协程  别名1 有多个入口的函数 别名2 可以暂停的函数(可以向暂停的地方传入值)


## 生成器 不仅可以产出值 还可以获得调用方的值
def get_func():
    url = yield  "www.baidu.com"
    print(url)
    yield 2
    yield 3
    return "boby"

if __name__ == "__main__":
    gen = get_func()
    #警告 生成器第一步启动 不能send非None 值 ,只能send (None) 或者 next(gen)
    gen.send(None)
    # 启动生成器的两种方式 next send
    #print(next(gen)) #获取到百度

    # send方法可以传值给生成器内部，同时还可以重启生成器执行到下一个 yield位置 并得到yield值
    gen.send("www.126.com") #传递给函数126网站
    print(next(gen))
