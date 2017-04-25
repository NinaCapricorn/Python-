# coding=utf-8


# 函数定义
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        print type(people)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


storage = {}
init(storage)
print storage
store(storage, 'Hello World')
store(storage, 'Hello Hi')
print storage


def inc(x):
    x += 1
    return x

foo = 10
inc(foo)
print foo


# 参数收集
def story(**kwds):  # 参数被收集为字典形式
    return 'Once upon a time, there was a' \
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):  # 参数被收集为元组形式
    if others:
        print 'Received redundant parameters:', others
    return pow(x, y)


# 位置参数 和 关键字参数
def interval(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


# 函数调用
def foo():
    """ Just a test on foo()... """
    print 'In foo()...'
    bar()


def bar():
    bar.__doc__ = 'Just a test on bar()...'
    print 'In bar()...'

foo()


# 参数传递
def convert(func, seq):
    return [func(eachNum) for eachNum in seq]
my_seq = [123, 45.67, -6.28e8, 99999999L]
print convert(int, my_seq)
print convert(long, my_seq)

print max((1, -2))



