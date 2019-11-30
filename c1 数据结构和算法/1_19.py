# 转换并同时计算数据

# 一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数
import os
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# 例子
# Determine if any .py files exist in a directory
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)

# 在使用一些聚集函数比如 min() 和 max() 的时候你可能更加倾向于使用生成器版本，
# 它们接受的一个 key 关键字参数或许对你很有帮助

# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
