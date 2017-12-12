 # 字典中的键 映射多个 值

d = {'a':[1,2,3],
      'b':[4,5,6]
}
from collections import defaultdict

#两种模式 一种列表 一种 集合
#列表模式
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a'].append(1)
print( d )
#集合模式

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['a'].add(3)
d2['a'].add(1)

print(d2)

