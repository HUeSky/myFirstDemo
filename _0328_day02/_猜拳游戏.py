import random

player01 = input('请输入石头（0）剪刀（1）布（2）：')
player01 = int(player01)
#  randint 随机出 0 1 2 三个数其中一个
computer = random.randint(0, 2)
# 补充判断知道计算机出什么
if computer == 0 :
    computerZhao = '石头'
elif computer == 1 :
    computerZhao = '剪刀'
else:
    computerZhao = '布'
print('计算机出了：%s' % computerZhao)
if (player01 == 0 and computer == 1) or (player01 == 1 and computer == 2) or (player01 == 2 and computer == 0):
    print('玩家赢')
elif player01 == computer:
    print('平局')
else:
    print('计算机赢了')
