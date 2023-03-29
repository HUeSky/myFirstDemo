import random
player, p, rebot = 0, 0, 0
for x in range(1, 101):
    player01 = random.randint(0, 2)  # 玩家随机出
    computer = random.randint(0, 2)  # randint 随机出拳（0）剪刀（1）布（2） 三个数其中一个
    if (player01 == 0 and computer == 1) or (player01 == 1 and computer == 2) or (player01 == 2 and computer == 0):
        player += 1  # player 赢
    elif player01 == computer:  # 平局
        p += 1
    else:  # rebot赢
        rebot += 1
print('玩家赢了%d次,平局了%d次，机器人赢了%d次' % (player, p, rebot))
