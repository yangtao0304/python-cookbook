# 查找最大或者最小的N个元素

# heapq模块有两个函数：nsmallest(), nlargest()

import heapq

'''
Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
    all k, counting elements from 0
The interesting property of a heap is that a[0] is always its smallest element.
'''

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# nlargest(n, iterable, key=None)
# Equivalent to : sorted(iterable, key=key, reverse=True)[:n]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


# -------------------------------------------------------------------
# 可接受关键字参数
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio,
                        key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio,
                           key=lambda s: s['price'])
print(cheap, expensive)


# -------------------------------------------------------------------
# 在一个集合中查找最小的或者最大的N个元素，可首先对数据进行堆排序
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)

# Transform list into a heap, in-place, in O(len(heap)) time.
heapq.heapify(heap)
print(heap)

# heappop(), 会将第一个最小的元素弹出来
# 然后用下一个最小的元素取代被弹出的元素，复杂度仅仅是 O(log(len(heap))) time
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)


# -------------------------------------------------------------------
'''
最后
1. 如果要查找的元素个数相对比较小时，函数nlargest(), nsmallest()是很合适的
2. 如果仅查找1个最大或者最小元素，使用max(), min()
3. 如果要查找的元素个数规模相当，通常排序后切片操作会更快，sorted(nums)[:N], sorted(nums)[-N:]
'''
