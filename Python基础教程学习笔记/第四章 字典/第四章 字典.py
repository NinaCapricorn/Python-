# coding=utf-8
from copy import deepcopy

people = {
    'Alice': {
        'phone': '0001',
        'addr': 'Foo Driver 23'
    },
    'Beth': {
        'phone': '1234',
        'addr': 'Bar Street 42'
    },
    'Ceil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = raw_input('Name(Alice,Beth,Ceil):')
key = raw_input('phone or addr? ')

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

format_name = "%s's %s is %s."
print format_name % (name, label, result)


# 字典的格式化字符串
template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print template % data


# copy deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')

# has_key
d = {'name': 'Eric'}
print d.has_key('name')
print 'name' in d

# item,iteritems
d = {'title': 'Python Web Site', 'url': 'http://www.python.org'}
print d.items()
print list(d.iteritems())
keys = d.keys()
print keys

d = {'title': 'Python Web Site', 'url': 'http://www.python.org'}
item = d.popitem()
print d

# setdefault
d = {}
d.setdefault('name', 'N')
print d
d['name'] = 'Alcie'
print d.setdefault('name')

# update
d = {'title': 'Python Web Site','url': 'http://www.python.org'}
x = {'title': 'Python', 'changed': 'Jan 19 19:43 2017'}
d.update(x)
print d

# values
d = {1: 1, 2: 2, 3: 3, 4: 1}
print d.values()  # [1,2,3,1]
