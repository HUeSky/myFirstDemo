# 将 helloword 打印5次
i = 1
while i <= 5:
    print('hello word%d' % i)
    i += 1

# 求1-100之和
num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1
#    print(str(sum))
print('和为：%d' % sum)
# 求1-100的偶数之和
num = 1
sum = 0
while num <= 100:
    if num % 2 == 0:
        sum += num
    #       print(str(sum))
    num += 1
print('和为：%d' % sum)
'''
x = 1
while x < 20:
    print('* ' * (x))
    x += 1
'''
a = 1  # 第几次循环
while a <= 5:  # 循环5此结束
    b = 1
    while b <= a:
        print('*', end=' ')
        b += 1
    print()
    a += 1
