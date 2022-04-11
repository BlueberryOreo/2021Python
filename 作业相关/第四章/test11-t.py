f = open("C:\\Users\\Administrator\\Desktop\\新建文件夹\\test.txt", "w+")

for n in range(15, 1000):
    sum1 = n // 15
    sum2 = n // 15
    if sum1 >= 3:
        sum1 += sum1 // 3
        if sum2 >= 5:
            sum2 += (sum2 // 5) * 2

    print(n, n // 15, sum1, sum2, file=f)
