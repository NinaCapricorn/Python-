# coding=utf-8
import math

# print 打印语句
name = 'Right'
sal = 'Mr.'
greeting = 'Hello,'
print greeting, sal, name         # Hello, Mr. Right
print greeting, ',', sal, name    # Hello, , Mr. Right
print greeting + ',', sal, name   # Hello,, Mr. Right
print greeting,
print sal                         # Hello, Mr.

# 赋值-序列解包
scoundrel = {'name': 'Bin',
             'girlfriend': 'Marion'}
item = scoundrel.popitem()
key, values = item
print key, values
# 赋值-自增
x = 1
x += 1
print x

# 条件语句 if/elif/else
num = input('Please input a number: ')
if num > 0:
    print '%d is positive' % num
elif num < 0:
    print '%d is negative' % num
else:
    print '%d is zero' % num

num = 10 if 1 < 10 else -1
print num

# 运算符 is/==
x = y = [1, 2, 3]
z = [1, 2, 3]
print x is y
x = [1, 2, 3]
print x is y
print x is z
print x == y
print x == z
print [1, 2, 3] < [1, 2, 4]

name = raw_input('Please input your name:') or 'unknown'
if name.endswith('Na'):
    print 'Hello, Mrs.Na'

# 循环-while/for
# 打印1-10
i = 1
while i in range(11):
    print i
    i += 1
for num in xrange(1, 11):
    print num

print ' '.isspace()  # 检查字符串中是否有空格


d = {'x': 1, 'y': 2, 'z': 3}
for key in d.keys():
    print 'd[%s] = %d' % (key, d[key])

for key, value in d.items():
    print key, ' corresponds to ', value

t1 = 'HelloWorld'
t = t1.replace('l', 't')
print t1, t

# 循环中else子句
for num in range(99, 81, -1):
    root = math.sqrt(num)
    if root == int(root):
        print num
        break
else:
    print 'None Found!'

while True:
    word = raw_input('Please enter a word: ')
    if not word:
        break
    print 'The word is :' + word

girls = ['alice', 'bernice', 'clarice', 'anna']
boys = ['chris', 'arnold', 'bob', 'dog']
letter_girls = {}
for girl in girls:
    letter_girls.setdefault(girl[0], []).append(girl)
print letter_girls
print [boy + '+' + girl for boy in boys for girl in letter_girls.get(boy[0], [])]

# 列表推导式
print [x*x for x in range(1, 10)]

