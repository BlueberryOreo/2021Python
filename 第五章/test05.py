import random

binary = bin(random.randint(2, 100))[2:]

count_z = 0
sum = 0
for i in binary:
    if i == "0":
        count_z += 1
    else:
        sum += 1

print(binary, "0:" + str(count_z), "sum =", sum)
