import math

n = int(input())

for i in range(2, n):
    is_prime = True
    for j in range(2, int(math.sqrt(i))):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i, end=" ")
