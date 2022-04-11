import math

r = int(input("r = "))
h = int(input("h = "))

n = math.ceil(20000 / (math.pi * r ** 2 * h))
print(n)
