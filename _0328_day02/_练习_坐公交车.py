balance = input('请输入余额：')
balance = float(balance)
if balance >= 2:
    print('可以坐车')
    seat = input('输入空座位数：')
    seat = int(seat)
    if seat != 0:
        print('有座位坐')
    else:
        print('没座位了，不乘车了')
else:
    print('钱不够坐车')
