n = int(input("Please input the number of numbers:").split("=")[1])
# print(n)

s = 0
for i in range(n):
    ss = input("Please input number {}:".format(i + 1))
    if s == "n=0":
        break
    s += int(ss)

print("sum =", s)
