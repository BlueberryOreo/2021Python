import random

rnd_lst = list(str(random.randint(100, 999)))
# print(rnd_lst)
temp = rnd_lst[0]
rnd_lst[0] = rnd_lst[2]
rnd_lst[2] = temp
out = 0
for i in range(len(rnd_lst)):
    out += int(rnd_lst[i]) * 10 ** (len(rnd_lst) - i - 1)
print(out)
