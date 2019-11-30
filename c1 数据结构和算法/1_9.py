# 查找两字典的相同点

a = {
    'x': 1,
    'y': 2,
    'z': 3}
b = {
    'w': 10,
    'x': 11,
    'y': 2}

# 为了寻找两个字典的相同点，可以简单的在两字典的 keys() 或者 items() 方法返回结果上执行集合操作
# find keys in common
a.keys() & b.keys()  # {'x', 'y'}
# find keys in a that are not in b
a.keys() - b.keys()  # {'z'}
# find (key, value) pairs in common
a.items() & b.items()  # {('y',2)}


# 这些操作也可以用于修改或者过滤字典元素。比如，假如你想以现有字典构造一个排除几个指定键的新字典
c = {key: a[key] for key in a.keys()-{'z', 'w'}}
print(c)


# -------------------------------------------------------------------
# 讨论
'''
1. 字典的keys()方法返回一个展现键集合的键视图对象，键视图的一个很少被了解的特性就是它也支持集合操作，比如集合交、并、差运算
2. 字典的items()方法返回一个包含（键，值）对的元素视图对象，这个对象同样支持集合操作，并且可以被用来查找两个字典有哪些相同的键值对
3. 字典的values()方法不支持集合操作，某种程度是因为值视图不能保证所有的值互不相同
'''