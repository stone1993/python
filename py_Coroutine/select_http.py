# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 8:25 PM
describe:
"""


import socket
from urllib.parse import urlparse
#import select    原生的select 本例中不使用 使用封装后的 selectors
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE  #封装select 后

# DefaultSelector 会根据平台选择我们用的IO复用模式
# windos 模式下 是 select
# linux/mac 模式下 是 epoll

#使用select 完成http 请求


selector = DefaultSelector() # 全局注册 selector

urls = ["http://www.baidu.com/"]
stop = False

class Fetcher:

    def connected(self,key ):
        #send 之前 我们需要在 selector 中注销掉 监控的事件
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        #注册事件 当socket 可读时返回
        selector.register(self.client,EVENT_READ,self.readable)

    def readable(self,key):
        d = self.client.recv(2048)

        if d:
            self.data += d
        else:   # 数据已经读完
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True


        pass
    def get_url(self,url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)  # 设置非阻塞

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass


        #参数1 文件描述符
        #参数2 事件类型  读事件/写事件
        #参数3 回调函数 回掉函数 位置放在 之前
        selector.register(self.client.fileno(),EVENT_WRITE,self.connected)


#写了回调 操作系统并不会帮我们自动执行回调 需要我们不断用select 判断 可读 可写
def loop():
    # 事件循环 不停的请求socket 状态 并调用回调函数。
    # 1 原生select模块 不支持 register模式
    # 2 socket 状态变化以后的回掉 是由程序员 自己完成的
     while not stop:
        ready = selector.select()
        for key,mask in ready:

            # key 的数据类型 SelectorKey = namedtuple('SelectorKey', ['fileobj', 'fd', 'events', 'data'])
            # key 也是  self.client.fileno() 的返回值

            call_back = key.data
            call_back(key)

    #回调函数 + 事件循环 + select(poll/epoll)
    # 特点 并发性高 函数中 充分都是消耗CPU的操作 事件循环 捕获请求 直接处理到 相应的回调函数，全程没有消耗多余的端口时间。
    # 单线程模式 省略了线程切换 开销
    # 切换线程的内存 远远高于 回调函数的占用内存
    # 线程一多,线程间切换就变得很慢，但回调函数 成千上万 都没内存消耗问题 以及线程切换问题，毕竟单线程模式。



if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com/")
    loop()

