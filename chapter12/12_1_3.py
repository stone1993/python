from threading import  Thread,Event
import time
"""其他线程需要判断某个线程是否已经到达过程中的某个点 用 Event
    Event 最好只用于一次性事件
    EVent 很难保证发起的事件清除一定在会在线程再次等待该事件前 被执行
"""
def countdown(n,eve):
    print("join countdown def")

    while n > 0:
        eve.set()
        time.sleep(3)
        n-=1
        print("______第{}次_______".format(5 -n,))





if __name__ == "__main__":
    eve = Event()
    n =5
    t = Thread(target=countdown,args=(n,eve,))
    t.start()
    print("event wait")
    while n >0:
        eve.wait()
        print("Eve wait end")
        eve.clear()

    print("event wait end")
    t.join()
    print("main end")
"""
总结：Event 最好只用于一次性事件
"""