money = float(input("请输入金额："))

count = 0
while True:
    ticket = 2
    if 0 <= count < 10:
        pass
    elif 10 <= count < 20:
        ticket = 2 * 0.95
    elif 20 <= count < 50:
        ticket = 2 * 0.8
    else:
        ticket = 2 * 0.5
    if money < ticket:
        break
    money = float("%.2f" % (money - ticket))
    count += 1

print("最多能坐{}次公交".format(count))
