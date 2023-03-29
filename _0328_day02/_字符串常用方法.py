"""
find 检测字符串是否在另一个字符串里面
如果找到就返回字符串最开始的位置的下标，找不到就返回-1
语法：name = ’asdfgh‘
    print(name.find("df"))

"""
name = 'qwerasdfertgfsa'
print(name.find('df'))
#  find 可以跟上查找的起始和结束位置，不写就是全部查找
print(name.find('df', 4, 12))
"""
index 查找某个字符串是否在另一个字符串中，作用和find一样。
如果找到返回位置下标，找不到就报错。
"""
print(name.index('df'))
print(name.index('df', 4, 12))  # 指定起始位置和结束位置

"""
count 某个字符串在另一个字符串中出现的次数
如果没出现就返回0
"""
print(name.count('s'))
print(name.count('df', 4, 12))
print(name.count('dsf', 4, 12))  # 找不到就返回0
"""
replace 替换
语法： 字符串名字.replace('要替换掉的内容', '替换的内容')
"""
newString = 'hello hehe, You hehe , I hehe.'
print(newString.replace('he', 'ha'))
print(newString.replace('he', 'ha', 2))  # 指定次数替换
"""
split 切割
以 str 为分隔符切⽚,如果 切割次数有指定值，则仅分隔 指定 个⼦字符串
"""
print(newString.split(' '))
print(newString.split(' ', 3))
"""
capitalize 首字母大写
"""
str = 'hello word!'
print(str.capitalize())
"""
title 把字符串每个字母的首字母大写
"""
print(str.title())
"""
startswith 判断是否以某个单词开头，区分大小写
endswith 判断是否以某个字符结尾
"""
print(str.startswith('he'))
print(str.startswith('He'))
print(str.endswith('word'))
print(str.endswith('!'))
"""
lower 将所以的大写变小写
upper  将所有的小写便大写
"""
print(str.upper())
print(str.lower())
"""
ljust 左对齐并填充长度
rjust 右对齐并填充长度
center 居中对齐并填充长度
"""
str = 'nihao'
print(str.ljust(10))
print(str.rjust(10))
print(str.center(10))

"""
strip 截取左边和右边的空白
"""
str = '    nihao    '
print(str.strip())  #'nihao'
print(str.lstrip())  # 'nihao    '
print(str.rstrip())  #'     nihao'
"""
partition 部分的意思，
作用是将一个字符串切割为三个部分
"""
str = 'asc lsy lyq!'
print(str.partition('lsy')) #('asc ', 'lsy', ' lyq!')
#当子串不存时
print(str.partition('ssl')) #('asc lsy lyq!', '', '')
"""
splitlines 按照换行符切割
"""
str = 'hello \n word'
print(str.splitlines())#['hello ', ' word']
"""
isalpha 如果字符串中都是字母则输出true，否则就是false
"""
print(str.isalpha())
"""
isdigit 判断是否都是数字
"""
num = '1235468791'
print(num.isdigit()) #True
print(str.isdigit()) #False
"""
isalnum 判断是否都是字母或者都是数字
"""
cha = '123asd123'
print(cha.isalnum())
"""
isspace 判断一个字符串是否为空白，不是null
"""
str = '      '
print(str.isspace())
#str = None
#'NoneType' object has no attribute 'isspace'
#print(str.isspace())
"""
join mystr 中每个字符后⾯插⼊str,构造出⼀个新的字符串
要插入的字符.join(被插入的字符串)
"""
str = '*'
mystr = ['my','name','lili']
print(str.join(mystr)) #my*name*lili