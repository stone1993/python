import time

def countdown(n):
    while n > 0:
        print ("T-minus" ,n)
        n -= 1
        time.sleep(5)

from threading import Thread

t = Thread(target = countdown,args = (3,))
t.start()
while True:
    time.sleep(2)
    if t.is_alive():    #判断线程状态
        print("线程还在继续")
    else:
        break

