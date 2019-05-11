# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 2:26 PM
describe: concurrent.future  python3.2中 引入 专门用于 线程池 进程池编程
        利于编写 多进程 多线程 代码
        为什么使用线程池 concurrent.future:
        1 控制线程数量 (semaphore 只能控制线程数量)
        2 主线程可以获取一个线程的状态 和 一个任务的状态,以及返回值
        3 当一个线程完成式,我们主线程能够立即知道。
        4 future 可以让多进程 多线程 编码接口一致
"""

from concurrent.futures import ThreadPoolExecutor ,as_completed,wait,FIRST_COMPLETED
from time import sleep

def get_html(times):

    sleep(times)
    print("get page {} success".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=5)

if __name__ =="__main__1":

    #通过 submit 提交 线程到线程池，submit 立即返回，非阻塞
    task1 = executor.submit(get_html,(3))
    task2 = executor.submit(get_html,(2))


    print(task1.done()) # done方法 判断任务有没有执行完成

    #cancel 取消执行线程
    # 取消成功返回 True 失败 返回 False
    # 当线程处于执行中 或者 执行完成 时，没法取消。
    # 当线程池 max_workers 设置小时，部分线程未执行可以取消。
    print(task2.cancel())

    #result 方法可以获取 线程返回值,此方法为阻塞方法
    print(task1.result())

if __name__ == "__main__2":
    #批量添加任务
    task_all = [executor.submit(get_html,(i)) for i in range(20)]
    # as_completed(task_all)
    # 通过 as_completed 获取 已经完成的future
    for future in as_completed(task_all):
        data = future.result()
        print("get {} page success".format(data))

if __name__ == "__main__3":
    # 通过 map 按照顺序获取 future

    for data in executor.map(get_html,[i for i in range(10)]):
        print("get {} page success".format(data))

if __name__ == "__main__":

    task_all = [executor.submit(get_html,(i)) for i in range(2)]

    #wait(task_all)  #阻塞所有子线程
    wait(task_all,return_when=FIRST_COMPLETED)#阻塞子线程 指到第一个完成
    print("main")

