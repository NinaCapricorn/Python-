# coding=utf-8
greeting = 'Hello,world!'

print greeting[0] + ',' + greeting[-1]  # 索引

# 分片 从 左->右 访问
print greeting[0:4]  # Hell
print greeting[:]  # Hello,world!
print greeting[:4]  # Hell
print greeting[3:]  # lo,world!
print greeting[1:1]  # 空
print greeting[2:1]  # 空
print greeting[0:14]  # Hello,world!
print greeting[0:10:3]  # Hlwl
print greeting[-2:-8:-2]  # drw

# 从 右->左 访问
print greeting[-5:-2]  # olr

print 'Hello' + 'World'
print 'Hello'*5
print [0]*10

fruits = ['apple', 'pear', 'banana']
fruit = raw_input('Please input: ')
print fruit + ' is in fruits? ' + str(fruit in fruits)

num = [0, 2, 3, 5, 10]
print max(num)
print min(num)
print len(num)


# 字符串转列表
print list('Hello')

# 列表转字符串
print ''.join(['h', 'o', 'o'])

