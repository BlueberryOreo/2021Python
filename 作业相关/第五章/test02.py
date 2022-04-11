# print(bin(int(input(), 16)))

hex = int(input(), 16)
binary = []

if hex == 0:
    binary.append(0)
else:
    while hex > 0:
        binary.append(hex % 2)
        hex //= 2

print("0b", end="")
for i in range(-1, -len(binary) - 1, -1):
    print(binary[i], end="")
