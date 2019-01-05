# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/05 6:13 PM
describe: 线程间通信 
"""

from time import sleep,time
from threading import Thread
from process_threading import variables


# 多线程通信方式1  全局变量
#detail_url_list = []
# 当多个线程调用一个变量 应维持变量的单例模式
# 运用 python 调包 天然的单例特性
def get_html_detail():
    detail_url_list = variables.detail_url_list
    "获取文章详情"
    while True:
        if len(detail_url_list):
            # 警告
            # 共享变量 存在线程安全性 多个线程同时pop时 不安全
            url = detail_url_list.pop()
            print(url)
            print("get html detail start")
            sleep(2)
            print("get html detail end")

def get_url_detail():
    "获取文章列表"
    detail_url_list = variables.detail_url_list
    print("get url detail start")
    for i in range(20):
        detail_url_list.append("www.baidu.com/{id}".format(id=i))
    print("get url detail end")

if __name__ == "__main__":
    url_detail = Thread(target=get_url_detail,)
    url_detail.start()
    for i in range(5):
        html_detail1 = Thread(target=get_html_detail, )
        html_detail1.start()

