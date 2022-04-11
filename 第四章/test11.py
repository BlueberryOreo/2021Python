import math

n = int(input())
while math.floor(n) != n:
    n = int(input("请输入一个整数！"))

sum1 = n // 15
sum2 = n // 15
if sum1 >= 3:
    sum1 += sum1 // 3
    if sum2 >= 5:
        sum2 += (sum2 // 5) * 2

print(sum1, sum2)

print("小明最多可以买{}瓶酱油".format(sum1 if sum1 > sum2 else sum2))
