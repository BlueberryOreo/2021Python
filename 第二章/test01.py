num = input("请输入一个三位整数：")
sum = 0
for i in num:
    sum += int(i)
print("{:>4}".format(sum))