import random

a = random.randint(5, 20)  # girls
b = random.randint(5, 20)  # boys

girls = a / (a + b) * 100
print("{:>8.2f}%".format(girls))