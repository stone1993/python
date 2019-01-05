# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 12:22 AM
describe:
"""


from time import sleep,time
from threading import Thread
from queue import Queue


# 多线程通信方式2  运用queue

# 当多个线程调用一个变量 应维持变量的单例模式
# 运用 python 调包 天然的单例特性
def get_html_detail(q):

    "获取文章详情"
    while True:
        url = q.get() #此方法阻塞 队列为空 阻塞住
        print(url)
        print("get html detail start")
        sleep(2)
        print("get html detail end")


def get_url_detail(q):
    "获取文章列表"

    print("get url detail start")
    for i in range(20):
        q.put("www.baidu.com/{id}".format(id=i))
    print("get url detail end")

if __name__ == "__main__":
    # queue 是线程安全的 多个线程同时操作queue 安全
    # 使用时很多锁机制 Queue 内部还有个queue ，调用的是双端队列，双端队列在字节码级别就是安全的
    # 其中 put_nowait 和 get_nowait 为异步方法 调用后不需要等待
    q = Queue(maxsize=100)
    url_detail = Thread(target=get_url_detail,args=(q,))
    url_detail.setDaemon(True)
    url_detail.start()
    for i in range(5):
        html_detail1 = Thread(target=get_html_detail, args=(q,))
        html_detail1.setDaemon(True)
        html_detail1.start()

    q.task_done()  #发送task_done 信号
    q.join() #队列阻塞线程退出 除非收到task_done 指令 本例中 在子线程中 调用task_done

