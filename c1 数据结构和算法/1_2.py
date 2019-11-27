# python的星号表达式

# -------------------------------------------------------------------
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

# 这里，值得注意的是解压得到的phone_numbers变量永远都是List类型
print(phone_numbers)


# -------------------------------------------------------------------
'''
讨论： 扩展的迭代解压语法是专门为不确定个数或任意个数元素的[可迭代对象]设计
'''
records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4),
           ]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# -------------------------------------------------------------------
# 可用于字符串的分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)


# -------------------------------------------------------------------
# 使用一个普通的废弃名称，如_或者ign丢弃某些元素
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *ign, (*_, year) = record
print(name, year)
