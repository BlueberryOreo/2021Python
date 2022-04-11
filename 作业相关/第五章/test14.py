import random

n = float(input("请输入金额："))

distance = [random.random() * 1.5 + 1.5 for x in range(29)]

# for d in range(len(distance)):
#     print(d, distance[d])
#
# print("sum =", sum(distance))

s = 0
flag1 = True
flag2 = False
count = 0

while True:
    if count == len(distance):
        break

    s += distance[count]
    if flag1:
        n -= 2
        flag1 = False
    elif flag2:
        n -= 1
        flag2 = False
    if s >= 5:
        s -= 5
        flag2 = True
    if n < 0:
        break
    count += 1

print("最多能坐{}站".format(count))

# ss = 0
# for c in range(count):
#     ss += distance[c]
# print(ss)
