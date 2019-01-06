# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 4:53 PM
describe:
"""

from multiprocessing import Process,Pool,cpu_count
from concurrent.futures import ProcessPoolExecutor
import os
import time

if __name__ == "__main__0":
    pid = os.fork()
    if pid == 0:
        print("I'm son pid is {} ,my father pid is {}".format(os.getpid(),os.getppid()))
    else:
        print("I'm father ,pid is {},my son pid is {}".format(os.getpid(),pid))



if __name__ == "__main__":
    def get_html(n):
        time.sleep(n)
        print("sub progress success {}".format(n))
        return n

    #使用普通进程
    processing = Process(target=get_html,args=(3,))
    processing.start()
    processing.join()

    # 使用进程池
    pool =Pool(cpu_count())  #设置进程池 大小按照CPU 数量
    result = pool.apply_async(get_html,args=(3,))

    #pool.close() #在调用 pool join方法之前 必须要先关闭线程池
    #pool.join()
    #print(result.get())


    # imap 方法 按照传入顺序返回
    # for result1 in pool.imap(get_html,[1,2,3]):
    #     print(result1)


    # imap_unordered 按照完成顺序返回
    for result in pool.imap_unordered(get_html,[5,7,1]):
        print("{} sleep success".format(result))
