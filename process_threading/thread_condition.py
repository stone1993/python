# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/06 1:13 AM
describe: python 多线程通讯方式之一 条件变量 
        用于复杂的线程间同步
        实现 两个线程间 一问一答
        
        condition 的 wait 和 notify 只有在 调用with/(调用acquire 记得要释放 release)
        
        Condition 具有两层锁，一把底层锁会在线程调用wait方法时释放
        上面的锁 会在每次调用wait时分配一把并放入condition 的等待队列中
        等待notify方法的唤醒

天猫精灵: 小爱同学
小爱: 在
天猫精灵:我们来对古诗吧
小爱:好的
天猫精灵:我住长江头
小爱:君住长江尾
天猫精灵:日日思君不见君
小爱:共饮长江水
天猫精灵:此水几时休
小爱:此恨何时已
天猫精灵:只愿君心似我心
小爱:定不负相思意
"""
from threading import Condition,Thread
class XiaoAi(Thread):
    def __init__(self,cond,*args,**kwargs):
        super().__init__(name="xiaoai",*args,**kwargs)
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}:在".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:好的".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:君住长江尾".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:共饮长江水".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:此恨何时已".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:定不负相思意".format(self.name))
            # self.cond.notify()
            # self.cond.wait()

class Tmall(Thread):
    def __init__(self,cond,*args,**kwargs):
        super().__init__(name="tmall",*args,**kwargs)
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}:小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:天猫精灵:我们来对古诗吧".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:我住长江头".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:日日思君不见君".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:此水几时休".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:只愿君心似我心".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:小爱同学".format(self.name))
            self.cond.notify()
            # self.cond.wait()



if __name__ == "__main__":
    condition = Condition()
    xiao = XiaoAi(condition)
    tmall = Tmall(condition)
    xiao.start()
    tmall.start()