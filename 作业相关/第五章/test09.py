n = int(input("请输入一个整数："))

f = open("./test.txt", "wt")

for i in range(2 * n - 1):
    count = 2 * n - 1 - abs(n - i - 1)
    # print(abs(n - i - 1))
    print("  " * (abs(n - i - 1)), end="", file=f)
    for j in range(count):
        print("*", end="   ", file=f)
    print(file=f)

f.close()