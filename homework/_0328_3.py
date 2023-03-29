i = 1
k = 1
while i <= 5:  # true输出前5行
    j = 1
    while j <= i:  # 前5行的*输出
        print('*', end=" ")
        j += 1
    i += 1
    print()
else:  # 前5行输出后执行下面的循环输出后4行
    while k < 5:
        j = 5
        while j > k:
            print('*', end=" ")
            j -= 1
        k += 1
        print()
