# 序列中出现次数最多的元素

# 解决方案：collections.Counter类
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# 出现频率最高的 3 个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]


# -------------------------------------------------------------------
# 讨论
'''
作为输入，Counter 对象可以接受任意的由可哈希(hashable)元素构成的序列对象
在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上
'''
word_counts['not']
# 1
word_counts['eyes']
# 8

# 如果你想手动增加计数，可以简单的用加法:
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

word_counts['eyes']
# 9

# 或者你可以使用update方法
word_counts.update(morewords)

# !! Counter实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合
a = Counter(words)
b = Counter(morewords)

c = a + b
print(c)
d = a - b
print(d)

# 毫无疑问，Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具
# 在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现
