# 字典排序

# 为了能控制一个字典中元素的顺序，你可以使用collections模块中的OrderedDict类
# 在迭代操作的时候，它会保持元素被插入时的顺序

import json
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])


# 序列化 (如果你想要精确控制以JSON编码后字段的顺序，可以先使用OrderedDict来构建这样的数据)
print(json.dumps(d))
print(type(json.dumps(d))) # str


# -------------------------------------------------------------------
'''
OrderedDict内部维护着一个根据键插入顺序排序的双向链表
每次当一个新的元素插入进来的时候，它会被放到链表的尾部，对于一个键的重复赋值不会改变键的顺序

需要注意的是，一个OrderedDict大小是普通字典的两倍，因为内部维护着另外一个链表
所以如果你要构建一个需要大量OrderedDict实例的数据结构的时候（比如读取100,000行CSV数据到一个OrderedDict列表中去）
那么你就得仔细权衡一下是否使用OrderedDict带来的好处要大过额外内存消耗的影响
'''
