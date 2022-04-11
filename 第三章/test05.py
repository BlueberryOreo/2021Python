import random

lst = [2 * random.randint(1, 10) - 1 for x in range(random.randint(5, 20))]
a = random.randint(0, 20)
print(lst, a)
print("a在列表中" if lst.count(a) != 0 else "a不在列表中")
