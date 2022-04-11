def output(m):
    for row in m:
        for col in row:
            print(col, end="\t")
        print()


"""
n = int(input("n = "))
while n % 2 == 0:
    print("n不为奇数，请重新输入：")
    n = int(input("n = "))

sum = n * (n ** 2 + 1) / 2
# print(sum)
lst = [[0 for index in range(n)] for index in range(n)]
index = 0
j = int((n + 1) / 2) - 1
lst[index][j] = 1
for x in range(2, n ** 2 + 1):
    if index - 1 < 0:
        if j == n - 1:
            index -= 1
            lst[index][j] = x
        else:
            index = n - 1
            j += 1
            lst[index][j] = x
    else:
        if j == n - 1:
"""

n = int(input("请输入一个整数："))


def function1(n):
    a = [[0 for x in range(n)] for x in range(n)]
    now = 1
    i = 0
    j = n // 2
    while now <= n * n:
        a[i][j] = now
        next_i = i - 1
        next_j = j + 1
        if next_i < 0:
            next_i = n-1
        if next_j > n-1:
            next_j = 0
        if a[next_i][next_j] != 0:
            next_i = i + 1
            next_j = j
        i = next_i
        j = next_j
        now += 1
    output(a)


def function2(n):
#your code begin
    lst = [[0 for j in range(n)] for i in range(n)]
    row, col = 0, n // 2
    lst[row][col] = 1
    for i in range(2, n * n + 1):
        n_row, n_col = (row + n - 1) % n, (col + 1) % n
        if lst[n_row][n_col] or row == 0 and col == n - 1:
            n_row, n_col = row + 1, col
        row, col = n_row, n_col
        lst[row][col] = i
    return lst
#your code end