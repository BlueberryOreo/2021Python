import math

flag = False

money = 200
count = 0
for i in range(1, math.ceil(money / 2)):
    for j in range(1, math.ceil(money / 3)):
        for k in range(1, math.ceil(money / 15)):
            if i * 2 + j * 3 + k * 15 == money:
                print("{}+{}+{}".format(k, j, i))
                count += 1
print(count)
