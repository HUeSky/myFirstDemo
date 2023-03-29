# 求闰年
y = input("请输入年份: ")
y = int(y)

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print('%d是闰年' % y)
else:
    print('不是闰年')
