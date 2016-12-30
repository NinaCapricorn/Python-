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

# 赋值、删除
names = ['Alica', 'April', 'Beth', 'Pencil']
del names[0]
names[1] = []
print names

name = list('Capricorn')
name[3:7] = list('tern4')  # 分片赋值
print name
name[:3] = []  # 删除
print name
name[1:1] = list('INSERT')  # 插入
print name

num = list([0, 2, 3, 5, 10])
num.append(5)
nums_add = [6, 7, 8]
num.extend(nums_add)
print num
nums_add[len(nums_add)+1:] = [0, 0, 0]
print nums_add

a = [1, 2, 3]
b = [4, 5, 6]
a[:] = a + b
print a
print b

nums = [1, 2, [1, 2], 4, 1]
print nums.count(1)
print nums.index(1)

nums = [1, 2, 3, 4]
nums.insert(0, 5)
nums[1:1] = [6, 7]
print nums


x = [1, 2, 3]
element_last = x.pop()  # 默认为最后一个元素
e = x.pop(0)  # 移除第一个元素
x.append(x.pop())
print x


x = [1, 2, 3, 4, 1]
x.remove(1)
print x

x = [1, 2, 3]
x.reverse()
y = list(reversed(x))
print x
print y
print x


nums = [5, 2, 9, 7]
nums.sort(cmp)
print nums


names = ['Apple', 'Pear', 'Banana', 'Durian', 'Peach']
names.sort(key=len, reverse=True)
print names

t = (12,)
print t
