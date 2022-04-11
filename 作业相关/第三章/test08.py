import math
import random


# 判断一个数是否为素数
def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, math.ceil(num / 2) + 1):
        if num % i == 0:
            return False
    return True


# for index in range(1, 100):
#     print(index, is_prime(index))
# 随机生成一个长度为10~100，范围在1~100之间的整数的列表用于测试
lst = [random.randint(1, 100) for i in range(random.randint(10, 100))]
prime_lst = []
for i in lst:
    if i in prime_lst:
        continue
    if is_prime(i):
        prime_lst.append(i)

count = 0
# available = {}  # 测试用字典，用于查看具体哪些素数可以表达为该列表中另外哪两个素数的和
for i in range(len(prime_lst)):
    for j in range(i + 1, len(prime_lst)):
        # print("index = {}, j = {}".format(index, j))
        if prime_lst[i] + prime_lst[j] in prime_lst:
            count += 1
            # available["{}+{}".format(prime_lst[index], prime_lst[j])] = prime_lst[index] + prime_lst[j]

print(prime_lst, count)
# print(available)
