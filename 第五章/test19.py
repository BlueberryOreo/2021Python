import random

n = int(input())

# h = random.randint(100, 1000)
h = 100
s = 0
last = 0

for i in range(n):
    last = 0.5 ** (i + 1) * h
    if i == 0:
        s += h
    else:
        s += last * 2

print(s, last)
