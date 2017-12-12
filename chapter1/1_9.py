
#查找两个字典 相同的 键 或者 值
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print( a.keys() & b.keys() ) #获取相同键

print( a.items() & b.items()) #获取相同的值