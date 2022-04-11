import random
import math

lst = [random.randint(0, 50) for i in range(random.randint(10, 20))]
lst.sort()
# print(lst, len(lst))
print(lst[math.ceil(len(lst) / 2) - 1])
