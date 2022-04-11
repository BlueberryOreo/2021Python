import random
import math

r = random.random() * 15 + 5
v = (4 / 3) * math.pi * r ** 3
print("{:>15.3f}{:>15.3f}".format(r, v))