#实现队列优先级 每次 pop 返回优先级最高那个

# 利用 heapq
import heapq
class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Item{!r}".format(self.name)

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

q = PriorityQueue()
q.push(Item("xl"),1)
q.push(Item("xll"),2)
q.push(Item("xlll"),4)

print (q.pop())
