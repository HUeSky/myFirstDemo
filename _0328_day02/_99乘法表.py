i = 1
while i<=99:
    j=1
    while j<=i:
        print('%-2d*%-02d=%-4d '%(j,i,j*i),end='')
        j+=1
    i+=1
    print()


