#
num1 = 100
num2 = 80
# 使用type查看变量类型 type(变量名)
print(type(num1))
# python中不用写变量类型 直接写变量加赋值
print('%d' % num1)
print('%2d' % num1)
print('%02d' % num1)
print('%-2d' % num1)
print('%d' % num1)

print('    *', end=' \n')
print('*********')
print('=' * 40, '\n姓名：李永奇\nQQ：1971226212\n公司地址：郑州\n','=' * 40)
print('请输入密码：')
passwd=input()
print('请输入取款金额：')
my=input()
print('取款金额为'+my+'元')
myName = 'zhansan'
age = 19
print('我的名字是%s,我今年%d岁了'%(myName,age))