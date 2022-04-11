import random


def output(m):
    count = 0
    for i in m:
        print("{:>5}".format(i), end=",")
        count += 1
        if count == 10:
            print()
            count = 0


a = set()
while len(a) < 100:
    a.add(random.randint(0, 1000))
b = set()
while len(b) < 100:
    b.add(random.randint(0, 1000))

print("A={")
output(a)

print("}\nB={")
output(b)
print("}")

union = list(a | b)
union.sort()
intersection = list(a & b)
intersection.sort()
answer1 = list(map(int, input("请输入A|B（A和B的并集）：").split()))
answer2 = list(map(int, input("请输入A&B（A和B的交集）：").split()))

count = 0
while True:
    answer1.sort()
    answer2.sort()
    if union == answer1 and intersection == answer2:
        print("回答正确！")
        break
    else:
        count += 1
        if count == 3:
            print("回答错误！正确答案：")
            print("A|B={")
            output(union)
            print("\n}\nA&B={")
            output(intersection)
            print("\n}")
            break
        print("回答错误！你还有{}次机会".format(3 - count))
        print("请修改你的答案：")
        answer1 = list(map(int, input("请输入A|B（A和B的并集）：").split()))
        answer2 = list(map(int, input("请输入A&B（A和B的交集）：").split()))
