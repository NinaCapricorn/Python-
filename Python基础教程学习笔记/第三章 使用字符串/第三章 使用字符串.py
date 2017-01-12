# coding=utf-8
import math
from string import maketrans

# 字符串格式化
print 'Price of an egg: $%d' % 42
print 'Price of an egg: $% 5d' % 42
print 'Price of an egg: $% 5d' % -42
print 'Price of an egg: $%+d' % 42

print 'Pi : %f' % math.pi
print 'Pi : %06.2f' % math.pi
print 'Pi : %.3f' % math.pi
print 'Pi : %.*f' % (2, math.pi)
print 'Pi : %10.2f' % math.pi
print 'Pi : %-10.2f' % math.pi
print 'Pi : %*.*f' % (5, 2, math.pi)

print '%.5s' % 'Hello,World!'

# 使用给定的宽度打印格式化后的价格列表
width = int(raw_input('Please input width: '))
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
format_item = '%-*s%*.2f'
print '=' * width
print header_format % (item_width, 'Item', price_width, 'Price')
print '-' * width
print format_item % (item_width, 'Apples', price_width, 0.4)
print format_item % (item_width, 'Pears', price_width, 0.5)
print format_item % (item_width, 'Dried Apricots(16 0z.)', price_width, 8)
print '=' * width

# find方法
longStr = 'With a moo-moo here, and a moo-moo there'
# 在整个字符串中查找
print longStr.find('moo')  # 7
print longStr.find('mo-moo')  # -1
# 在子串中查找，需要提供起始、结束位置
print longStr.find('moo', 7)  # 7
print longStr.find('moo', 11, 13)  # -1

# join方法
seq = ['Hello', 'World', '!']
print ' '.join(seq)
dirs = ['', 'Users', 'lenovo', 'Desktop', 'Python']
print 'C:' + '\\'.join(dirs)

# replace方法
raw_string = 'Hello , one world!'
print raw_string.replace('one', 'My')
print raw_string.lower()
print raw_string

# split方法
raw_str = r'C:\Users\nenovo\Desktop\study'
print raw_str.split('\\')

# strip方法
raw_string = '  Hello,world!  '
print raw_string.strip()
print '  ***SPRING * for * everyone!!! ** '.strip(' *!')

# translate方法
table = maketrans('cs', 'kz')
raw_string = 'this is an incredible test.'
print raw_string.translate(table)
