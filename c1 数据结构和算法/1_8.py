# 字典的运算

# ？？？怎么样在数字字典中执行一些计算操作（比如求最小值、最大值、排序等等）

prices = {'ACME': 45.23,
          'AAPL': 612.78,
          'IBM': 205.55,
          'HPQ': 37.20,
          'FB': 10.75
          }

# 通常需要使用zip()函数先将键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 类似，可以使用zip()和sorted()函数来排列字典数据

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 需要注意的是，zip()函数创建的是一个只能访问一次的迭代器
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence


# -------------------------------------------------------------------
# 讨论
# 如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值
print(min(prices))  # return 'AAPL'
print(max(prices))  # return 'IBM'

# 使用字典的values()方法解决
print(min(prices.values()))
print(max(prices.values()))

# 你可能还想要知道对应的键的信息（比如哪种股票的价格是最低的？）
# 你可以在min()和max()函数中提供key函数参数来获取最小值或者最大值对应的键的信息
print(min(prices, key=lambda k: prices[k]))  # return 'FB'
print(max(prices, key=lambda k: prices[k]))  # return 'AAPL'
# 但是，如果还想要得到最小值，又得执行一次查找操作
min_value = prices[min(prices, key=lambda k:prices[k])]


prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(),prices.keys())))
print(max(zip(prices.values(), prices.keys())))
