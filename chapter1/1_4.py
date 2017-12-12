#查找最大元素/ 最小的 N 个元素
import  heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print ("最大的3个元素",heapq.nlargest(3,nums))
print("最小的3个元素",heapq.nsmallest(3,nums))


#在复杂的数据结构中 查找 最大的N个元素

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

expensive = heapq.nlargest(3,portfolio,key=lambda x: x['price'])
print("expensive is ",expensive)