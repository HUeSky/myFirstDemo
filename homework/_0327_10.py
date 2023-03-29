print('请输入用户名：')
name = input()
print('请输入密码：')
passwd = input()
if name == "123456" and passwd == "456789":
    print('亲爱的%s，欢迎登录千峰云学习平台'%name)
else:
    print('账号或密码错误')