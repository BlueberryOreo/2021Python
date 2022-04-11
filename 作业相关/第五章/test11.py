import random

n = int(input())
a = random.randint(0, 9)
s = 0
expression = ""
for i in range(n):
    for j in range(i + 1):
        expression += str(a)
    expression += "+" if i != n - 1 else ""
print(expression, eval(expression))
