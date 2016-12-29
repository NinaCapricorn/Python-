# coding=utf-8
# 以正确的宽度在居中的盒子内打印一个句子

sentence = raw_input('Sentence: ')
screen_width = 80
text_width = len(sentence)
box_width = text_width + 10
left_margin = (screen_width - box_width)/2

print ' '*left_margin + '+' + '-'*box_width + '+'
print ' '*(left_margin+5) + '|' + ' '*text_width + '|'
print ' '*(left_margin+5) + '|' + sentence + '|'
print ' '*(left_margin+5) + '|' + ' '*text_width + '|'
print ' '*left_margin + '+' + '-'*box_width + '+'

# 成员资格 in运算符
students = ['Pear', 'Apple', 'Tree']
isTrue = 'Pear' in students
print isTrue
print type(isTrue)
