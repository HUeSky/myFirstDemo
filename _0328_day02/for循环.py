'''
语法： for 临时变量 in 列表或字符串等：
          满足条件时执行的代码
     else：
          循环不满住是执行的代码

break：跳出循环
continue：跳出本次循环
'''
# 求1-100之和
x = 0
for i in range(1,101):
     x += i
print(x)

# 测试break
name = 'qwertyu'
for a in name:
     if a =='t':
          break
     else:
          print(a)

# 测试continue
sname = 'asdfghjkl'
for b in sname:
     if b == 'g':
          continue
     else:
          print(b,end=' ')
print()

zhu={1,2,3,4,5,6,7,8,9}
for x in zhu:
     for c in zhu:
          x = int(x)
          c = int(c)
          if x < c:
              continue
          print('%d*%d=%-2d'%(c,x,x*c),end=' ')

     else:
          print()