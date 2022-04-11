n = int(input("请输入一个10-50之间的整数："))
while n < 10 or n > 50:
    n = int(input("输入的数字不在10-50范围内，请重新输入："))

print(n)
