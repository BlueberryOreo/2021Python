num = int(input())

binary = []

if num == 0:
    binary.append(0)
else:
    while num > 0:
        binary.append(num % 2)
        num //= 2

print("0b", end="")
for i in range(-1, -len(binary) - 1, -1):
    print(binary[i], end="")
