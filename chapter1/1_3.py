from  collections import deque

#构建固定大小的队列，当队列满了是，新增加数据，最前面的数据丢掉
ll = deque(maxlen=6)
ll.append(1)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(55)
ll.append(12)
ll.append(6)
print( ll)