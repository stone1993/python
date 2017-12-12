#在数据结构中 进行计算操作
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

prices_sort =  sorted(zip(prices.values(),prices.keys()))
print (prices_sort)

#需要注意的是 zip() 函数创建的是一个只能访问  一次 !!! 的迭代器。
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
#print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

print (min(prices,key=lambda x: prices[x]))