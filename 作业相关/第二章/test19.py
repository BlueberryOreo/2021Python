import math

a = list(map(float, input().split(" ")))
b = list(map(float, input().split(" ")))

aM = math.sqrt(a[0] ** 2 + a[1] ** 2)
bM = math.sqrt(b[0] ** 2 + b[1] ** 2)
mult = a[0] * b[0] + a[1] * b[1]

cos = mult / (aM * bM)
print(cos)
