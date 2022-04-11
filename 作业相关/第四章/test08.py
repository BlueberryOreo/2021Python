import random
import os


# 找出两个数的最大公因数
def max_factor(a, b):
    while True:
        c = a % b
        a = b
        b = c
        if b == 0:
            return a


# 判断一个分数是否为无限循环小数
def is_infinity(nominator, denominator):
    m_factor = max_factor(nominator, denominator)
    nominator //= m_factor
    denominator //= m_factor

    while denominator % 5 == 0:
        denominator /= 5

    while denominator % 2 == 0:
        denominator /= 2

    if denominator == 1:
        return False
    else:
        return True


n = int(input("请输入练习次数："))
sign = ["+", "-", "*", "/"]
right = 0
for i in range(n):
    sign_index = random.randint(0, 3)
    num_left = random.randint(0, 100)
    num_right = random.randint(0, 100)
    # num_left = 0
    # num_right = 5
    o = sign[sign_index]
    if o == "/":
        while num_right == 0 or is_infinity(num_left, num_right):
            num_left = random.randint(0, 100)
            num_right = random.randint(0, 100)

    answer = eval(str(num_left) + o + str(num_right))
    if int(answer) == answer:
        answer = int(answer)
    # print(answer)

    result = input("%d%s%d="%(num_left, o, num_right))
    if result == str(answer):
        print("回答正确")
        right += 1
    else:
        print("回答错误，正确答案：", answer)
    if i < n - 1:
        print("还有{}道题".format(n - i - 1))
        print("=" * 20)
print("本次练习的正确率为{:.2f}%".format(right / n * 100))
os.system("pause")
