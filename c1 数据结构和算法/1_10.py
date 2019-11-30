# 删除序列相同元素并保持顺序

# 解决方案：如果序列上的值都是hashable类型，那么可以很简单的利用集合或者生成器来解决这个问题


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# 这个方法仅仅在序列中元素为hashable的时候才管用
# 如果你想消除元素是不可哈希（比如dict类型）的序列，你需要修改代码如下：
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# 这里的key参数指定了一个函数，将序列元素转换成hashable类型
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))


# -------------------------------------------------------------------
# 如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合
a = [1, 5, 2, 1, 9, 1, 5, 10]
set(a)
# {1, 2, 10, 5, 9}
# ! 然而，这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱。而上面的方法可以避免这种情况


# -------------------------------------------------------------------
# 在本节中我们使用了生成器函数让我们的函数更加通用，不仅仅是局限于列表处理
# 比如，如果如果你想读取一个文件，消除重复行，你可以很容易像这样做:
with open(somefile, 'r') as f:
    for line in dedupe(f):
        ...
