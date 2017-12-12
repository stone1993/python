from collections import OrderedDict
# 带顺序的字典
d = OrderedDict()

d['a']=1
d['b']=2
d['c']=3
d['d']=4
d['e']=5
for key,value in d.items():
    print("key",key,"values",value)

#json 顺序可控制

import json
print(json.dumps(d))
