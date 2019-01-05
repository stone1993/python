# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 2:04 AM
describe: Semaphore 用于控制进入数量的锁

 文件 读写 写:一般只用于一个线程写
          读:可以允许多个读
          
爬虫 控制爬虫数量,避免数量过多,触发反爬虫
"""
import threading
import time

class HtmlSpider(threading.Thread):
    def __init__(self,url,sem,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.url = url
        self.sem = sem
    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self,sem,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.sem = sem
    def run(self):
        for i in range(20):
            sem.acquire() #控制进入的数量 每acquire 每申请一个锁,当锁数量等于限制 阻塞住
            html_thread =HtmlSpider("http:www.baidu.com/{i}".format(i=i),self.sem)
            html_thread.start()

if __name__ == "__main__":
    sem = threading.Semaphore(3)
    producter = UrlProducer(sem)
    producter.start()