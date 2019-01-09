# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2019/01/09 1:52 AM
describe: 协程的 嵌套 以及取消
"""
import asyncio

loop = asyncio.get_event_loop()

#loop.run_until_complete() # 当协程结束 停止

# run_until_complete 如何实现停止
#future.add_done_callback(_run_until_complete_cb) 添加了 当协程结束 的 回调函数
# 在回调函数中 _run_until_complete_cb  将future     fut._loop.stop()  的事件循环停止了

#1 loop 放在了future中 ，future之前也放入了loop中，产生闭环关系

#loop.run_forever() #永久运行
if __name__ == "__main__":
    async def get_html(n_sleep):
        print("waiting")
        await asyncio.sleep(n_sleep)
        print("ending")

    loop = asyncio.get_event_loop()
    task = [get_html(i) for i in range(2,5)]
    try:
        loop.run_until_complete(asyncio.wait(task))
    except KeyboardInterrupt as e:      #捕获按键异常并停止
        all_task = asyncio.Task.all_tasks()
        for task in all_task:
            task.cancel()      #取消协程
            print(task.cancel())    #取消成功 返回True
        loop.stop()            #终止事件循环
        loop.run_forever()      #必须要重启启动事件循环 否则有异常
    finally:
        loop.close()

