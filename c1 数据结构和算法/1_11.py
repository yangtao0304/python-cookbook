# 命名切片

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

print(cost)

# 使用切片
SHARES = slice(20, 23)
PRICE = slice(32, 37)
cost = int(record[SHARES]*record[PRICE])

# 具体使用方法
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
items[2:4]
# [2, 3]
items[a]
# [2, 3]
items[a] = [10, 11]
items
# [0, 1, 10, 11, 4, 5, 6]
del items[a]
items
# [0, 1, 4, 5, 6]


# 如果你有一个切片对象a，你可以分别调用它的 a.start , a.stop , a.step 属性来获取更多的信息

a = slice(5, 50, 2)
a.start
a.stop
a.step


# 你还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序列上,
# 这个方法返回一个三元组(start, stop, step) ，所有值都会被合适的缩小以满足边界限制，
# 从而使用的时候避免出现 IndexError 异常
s = 'HelloWorld'
a.indices(len(s))
# (5,10,2)
for i in range(*a.indices(len(s))):
    print(s[i])
# W
# r
# d
