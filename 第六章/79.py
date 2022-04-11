import random

tup = tuple(random.randint(10, 30) for i in range(random.randint(30, 40)))

large = max(tup)
small = min(tup)
average = sum(tup) / len(tup)

print("max =", large, "min =", small, "average =", average)
