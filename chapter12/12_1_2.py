import time

def countdown(n):
    while n > 0:
        print ("T-minus" ,n)
        n -= 1
        time.sleep(5)

from threading import Thread

#daemon 守护进程 一直不断运行的后台程序
# 但是，主进程结束，守护进程会被销毁
# 守护线程无法被连接
# t = Thread(target=countdown,args=(3,),daemon=True)
# t.start()
# t.join()

# 线程函数无法实现 终止线程 给线程发信号 调整线程调度属性

#编写线程类 实现轮询退出线程
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self,n):
        while self._running and n >0:
            print ("T-minus",n)
            n -= 1;
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run,args=(10,))
t.start()
time.sleep(4)
c.terminate()
t.join()
