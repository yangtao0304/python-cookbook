# 实现一个优先级队列

'''
??? 如何实现一个按照优先级排序的队列，并且在这个队列上每次pop操作总是返回优先级最高的元素
'''

# 解决方案：下面的类利用heapq模块实现了一个简单的优先级队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 先判断优先级大小，同优先级条件下，先进先出
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        heapq.heappop(self._queue)[-1]

# 下面是它的使用方式


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()
q.pop()
