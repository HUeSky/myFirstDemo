print('请输入用户名：')
name = input()
print('请输入密码：')
passwd = input()
if name == "123456" and passwd == "456789":
    print('亲爱的%s，欢迎进入python世界' % name)
else:
    print('账号或密码错误')
