import random

num = random.randint(0, 100)
count = 1
while num != 50:
    num = random.randint(0, 100)
    count += 1
print(count)