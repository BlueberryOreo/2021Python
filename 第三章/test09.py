# 筛法求质数
lst = [1 for i in range(50)]  # 先建立一个全部为1的列表
for i in range(2, 51):
    for j in range(2, 51):
        if i * j <= 50:
            lst[i * j - 1] = 0  # 将下标+1的倍数的元素标记为0，即把合数筛掉

count = 0
for i in range(len(lst)):
    if i == 0:
        continue
    # 输出1所在的下标+1，得到素数
    if lst[i] == 1:
        print(i + 1, end="\t")
        count += 1
    # 每输出五个换一行
    if count == 5:
        print()
        count = 0
