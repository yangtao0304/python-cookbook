# 保留最后N个元素

# 使用到collections.deque提供的双端队列

from collections import deque

'''
tips: 我们在写查询元素的代码时，通常使用包含yield的生成器函数
这样可以将[搜索过程代码]和[使用搜索结果代码]解耦
'''
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # 生成器函数
            yield line, previous_lines
        previous_lines.append(line)


# Example use
# if __name__ == "__main__":
#     # f = open(r'somefile.txt')
#     f = ['python'+str(i) for i in range(50)]
#     for line, prevlines in search(f, 'python', 5):
#         for pline in prevlines:
#             print(pline)
#         print(line)
#         print('-' * 20)