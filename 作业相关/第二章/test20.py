import math
import random

a = random.random() * 40 + 10
b = random.random() * 40 + 10

z = "{:.2f}+{:.2f}i".format(a, b)
m = math.sqrt(a ** 2 + b ** 2)
if a == 0:
    theta = math.pi / 2 if b > 0 else -math.pi / 2
else:
    theta = math.atan(b / a)
print("{:>7}{:>7.2f}{:>7.2f}".format(z, m, theta))
