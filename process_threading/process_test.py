# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 4:25 PM
describe: 多进程与 多线程 
消耗CPU的操作 多用于多进程 因为 GIL锁的原因  多线程不能充分利用多核CPU
对于IO操作,使用多线程 进程切换代价高于线程切换 

"""
from concurrent.futures import ThreadPoolExecutor,as_completed,ProcessPoolExecutor
import time
if __name__ == "__main__1":
    def fib(n):
        if n<=1:
            return 1
        else:
            return fib(n-1)+fib(n-2)

    with ThreadPoolExecutor(3) as executor:

        start = time.time()
        all_task = [executor.submit(fib,(num)) for num in range(25,30)]
        for future in as_completed(all_task):
            data = future.result()
            print(data)
        print("ThreadPool use time is {}".format(time.time()-start))

    with ProcessPoolExecutor(3) as executor:
        start = time.time()
        all_task = [executor.submit(fib,(num)) for num in range(25,30)]
        for future in as_completed(all_task):
            data = future.result()
            print(data)
        print("ProcessPool use time is {}".format(time.time()-start))

        #
        # ThreadPool use time is 0.5879619121551514
        # ProcessPool use time is 0.38596606254577637
        # 结论:消耗CPU 操作 多进程耗时小于多线程 多进程能充分利用CPU
        #
if __name__ =="__main__":
    def random_sleep(n):
        print("sleep time ",n)
        time.sleep(n)
        print("end sleep time ", n)


    with ThreadPoolExecutor(3) as executor:

        start = time.time()
        all_task = [executor.submit(random_sleep,(num)) for num in range(1,5)]
        for future in as_completed(all_task):
            data = future.result()
            print(data)
        print("ThreadPool use time is {}".format(time.time()-start))

    with ProcessPoolExecutor(3) as executor:
        start = time.time()
        all_task = [executor.submit(random_sleep,(num)) for num in range(1,5)]
        for future in as_completed(all_task):
            data = future.result()
            print(data)
        print("ProcessPool use time is {}".format(time.time()-start))



        # ThreadPool use time is 5.009896278381348
        # ProcessPool use time is 5.019981622695923
        # 结论:消耗IO操作 多线程耗时小于多进程
