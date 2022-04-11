import random

lst = [random.randint(1, 10) ** 2 for i in range(random.randint(5, 20))]
lst.sort()
print(lst)