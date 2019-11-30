# 排序不支持原生比较的对象


from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


sort_notcompare()

# 另外一种方式是使用 operator.attrgetter() 来代替 lambda 函数
users = [User(23), User(3), User(99)]
print(sorted(users, key=attrgetter('user_id')))

# 讨论
'''选择使用 lambda 函数或者是 attrgetter() 可能取决于个人喜好
但是， attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较
'''
# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

# 同样需要注意的是，这一小节用到的技术同样适用于像 min() 和 max() 之类的函数
min(users, key=attrgetter('user_id'))
max(users, key=attrgetter('user_id'))
