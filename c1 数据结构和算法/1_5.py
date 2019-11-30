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

    # O(log(N))
    def push(self, item, priority):
        # 先判断优先级大小，同优先级条件下，先进先出
        # heappop()总是返回“最小的”元素
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    # O(log(N))
    def pop(self):
        heapq.heappop(self._queue)[-1]

# 下面是它的使用方式


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()
q.pop()


# -------------------------------------------------------------------
# Item不支持排序
a = Item('foo')
b = Item('bar')
a < b
# TypeError: unorderable types: Item() < Item()

# 若使用元组(priority, Item), 只要两个元素的优先级不同就可以比较
# 但是如果两个元素优先级一样，那么就会出错
a = (1, Item('foo'))
b = (2, Item('bar'))
a < b
# True
c = (1, Item('grok'))
a < c
# TypeError: unorderable types: Item() < Item()

# 通过引入index变量组成三元组(priority, index, item), 就能很好避免上面的错误
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
a < b
# True
a < c
# True


# -------------------------------------------------------------------
# 如果你要想在多个线程中使用同一个队列，那么你需要增加适当的锁和信号量机制