name = ["张飞", "李大刀", "李墨白", "王老虎", "雷小米"]
advanced_mathematics = [78, 92, 84, 50, 99]
linear_algebra = [75, 67, 88, 50, 98]
sum = []
for i in range(5):
    sum.append(advanced_mathematics[i] + linear_algebra[i])

# 利用python存储数据的特性，通过内存地址连接分数和姓名下标
ids = [i for i in sum]

sum.sort()
for i in range(len(sum) - 1, -1, -1):
    print(name[ids.index(sum[i])], sum[i])
