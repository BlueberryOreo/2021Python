import random

tup = tuple(random.randint(1, 5) for i in range(20))
lst = []

for i in tup:
    if i not in lst:
        lst.append(i)
    else:
        continue

print(tup)
print(lst)
