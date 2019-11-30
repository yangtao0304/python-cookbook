# 字典中的键映射多个值

'''
??? 怎样实现一个键对应多个值的字典？(multidict)
'''

# 可以很方便的使用collections模块中的defaultdict来构造这样的字典
# defaultdict的一个特征是它会自动初始化每个key刚开始对应的值，所以你只需要关注添加元素操作了

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

# 需要注意，defaultdict会自动为将要访问的键（就算目前字典不存在这样的键）创建映射实体
# 这可以在一个普通的字典使用setdefault()方法来代替
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

# 自己实现一个多值映射字典
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
