
import  threading
import time
"""
线程重复 通知事件 用 Condition
"""

class PeriodicTimer:
    def __init__(self,interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()


    def run(self):
        """运行定时器，并在每个间隔之后 通知 所有的线程"""
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^=1
                self._cv.notify_all()

    def wait_for_tick(self):
        """ 等待定时器的下一次通知 """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

ptimer = PeriodicTimer(3)
ptimer.start()

def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print("T-minus",nticks)
        nticks -=1
def countup(nticks):
    n = 0
    while n < nticks:
        ptimer.wait_for_tick()
        print("counting",n)
        n +=1

threading.Thread(target=countdown,args=(3,)).start()
threading.Thread(target=countup,args=(3,)).start()





