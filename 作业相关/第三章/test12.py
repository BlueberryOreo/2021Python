import random


# 格式化输出一个矩阵
def output(m):
    for row in m:
        for col in row:
            print(col, end="\t")
        print()


matrix = [[random.random() * 99 + 1 for cow in range(4)] for rol in range(4)]
output(matrix)
print()
for i in range(len(matrix)):
    for j in range(i, len(matrix[i])):
        # print(matrix[index][j], matrix[j][index])
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp
        # print(matrix[index][j], matrix[j][index])

output(matrix)