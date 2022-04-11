n = int(input("n="))

print("\t", end="")
for i in range(1, n + 1):
    print("{:<4}".format(i), end="")

print()

for i in range(1, n + 1):
    print("{:<4}".format(i), end="")
    for j in range(1, i + 1):
        print("{:<4}".format(i * j), end="")
    print()
