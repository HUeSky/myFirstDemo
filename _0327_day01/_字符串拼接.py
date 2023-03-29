name = 'zhangsan'
age = 20
print('name=%s,age=%d' % (name,age))
name2 = 'lesi'
print('两个人的名字是：'+name+","+name2)
print('name='+name+',age='+str(age))
#float =>int str=> int
a=int(3.14)
b=int('1')
print(type(a))
print(type(b))
print(a)
print(b)
#转float
c = float(3)
d = float('3.14')
print(type(c))
print(type(d))
print(c)
print(d)

# 转str
e = str(100)
f = str(3.14)
print(type(e))
print(type(f))
print(e)
print(f)

# bool里面只要不空，或者不是0 就返回true
q = bool(1)
w = bool(0)
print(q)
print(w)