# coding=utf-8
# 根据给定的年月日以数字形式打印出日期
# raw_input: 不管用户输入什么类型，都转换成字符串
# input: 合法的python表达式（自带类型）

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# 以1~31的数字作为结尾的列表
endings = ['st', 'nd', 'rd'] + 17*['th'] + \
          ['st', 'nd', 'rd'] + 7*['th'] + \
          ['st']

year = raw_input('Year: ')
month = raw_input('Month: ')
day = raw_input('Day: ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
day_name = day + endings[day_number-1]

print day_name + ' ' + month_name + ',' + year
