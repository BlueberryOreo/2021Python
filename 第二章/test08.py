import random
import math

r = random.random() * 15 + 5
h = 10
v = math.pi * r ** 2 * h / 3
print("{:>10.3f}{:>10.3f}{:>10.3f}".format(r, h, v))