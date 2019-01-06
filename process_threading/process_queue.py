# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 5:30 PM
describe: 多进程编程通信的queue
"""
from multiprocessing import Queue,Process,Manager,Pool,Pipe
# 多进程编程 通信 queue 不能用 线程的Queue
#from queue import Queue  此队列 为 线程间的消息队列 多进程不能使用

# 多进程通讯 不能采用 共享变量 因为 每个进程都是彼此独立的

#利用进程间的queue
if __name__ == "__main__1":

    q = Queue(maxsize=10)
    def producter():
        global q
        q.put("a")

    def customer():
        global q
        value = q.get()
        print("customer get {}".format(value))


    p = Process(target=producter)
    c = Process(target=customer)
    p.start()
    c.start()
    p.join()
    c.join()

#进程池通讯 不能采用 multiprocessing.queue
# 应该使用 multiprocessing.Manager 生成的对象 的Queue

if __name__ == "__main__2":
    q = Manager().Queue()


    def producter():
        global q
        q.put("b")


    def customer():
        global q
        value = q.get()
        print("customer get {}".format(value))

    pool = Pool(3)
    pool.apply_async(producter)
    pool.apply_async(customer)
    pool.close()
    pool.join()


#  利用管道 pipe 在多进程间通讯
# pipe 性能比 queue 好
if  __name__ == "__main__3":

    recv_pipe,send_pipe = Pipe()

    def producter(p):
        p.send("asd")



    def customer(p):
        value = p.recv()
        print("customer get {}".format(value))


    p = Process(target=producter,args=(send_pipe,))
    c = Process(target=customer,args=(recv_pipe,))
    p.start()
    c.start()
    p.join()
    c.join()

if __name__ == "__main__":
    process_dict = Manager().dict()
    # 多进程间 共享内存 不仅可以是字典 还具有 以下数据结构
    # Barrier BoundedSemaphore Condition Event Lock Namespace Queue RLock
    # Semaphore Array Value  list
    # 运用共享内存 的变量 需要注意 运用 Condition Event Lock Rlock 相关 给数据做好同步


    def producter(d):
        d.update({"ass":12})


    def customer(d):
        value = d["ass"]
        print("customer get {}".format(value))


    p = Process(target=producter,args=(process_dict,))
    c = Process(target=customer,args=(process_dict,))
    p.start()
    c.start()
    p.join()
    c.join()