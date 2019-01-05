# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/05 4:52 PM
describe: 对于IO操作来说 线程与进程差异不大，单线程调用更轻量级
我们编写两个函数 让他们 以线程形式 并行运行
get_html_detail 获取文章列表
get_url_detail 获取文章内容
"""
from time import sleep,time
# from threading import Thread
import threading


def get_html_detail(url):
    print("get html detail start")
    sleep(2)
    print("get html detail end")

def get_url_detail(url):
    print("get url detail start")
    sleep(2)
    print("get url detail end")

#线程时实现方式1
if __name__ == "__main1__":
    start = time()
    t1 = Thread(target=get_html_detail,args=("",))
    t2 = Thread(target=get_url_detail, args=("",))
    t1.setDaemon(True) # 当不设置守护进程时 主线程退出后 子线程继续执行，设置后 主线程 退出 子线程也退出
    t2.setDaemon(True) # 当不设置守护进程时 主线程退出后 子线程继续执行，设置后 主线程 退出 子线程也退出
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("use time is {}".format(time()-start))

#方式2 通过继承Thread 重载 run方法 实现多线程
if __name__ == "__main__":

    class GetHtmlDetail(threading.Thread):
        def __init__(self,name):
            super().__init__()
            self.name = name
        def run(self):
            print("get html detail start")
            sleep(2)
            print("get html detail end")

    class GetUrlDetail(threading.Thread):

        def __init__(self,name):
            super().__init__()
            self.name = name
        def run(self):
            print("get url detail start")
            sleep(2)
            print("get url detail end")

    t1 = GetHtmlDetail(name="html")
    t2 = GetUrlDetail(name="url")
    t1.start()
    t2.start()





