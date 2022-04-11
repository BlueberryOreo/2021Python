
def output(m: list):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end="\t")
        print()


def add(a: list, b: list):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return

    row = len(a)
    col = len(a[0])
    c = [[0 for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            c[i][j] = a[i][j] + b[i][j]

    return c


def set_matrix(matrix: list, name: str):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(input("Please input {}[{}][{}]".format(name, i, j)))


if __name__ == "__main__":
    n = int(input("Please input the number of rows："))
    m = int(input("Please input the number of columns："))

    matrix_a = [[0 for i in range(m)] for j in range(n)]
    matrix_b = [[0 for i in range(m)] for j in range(n)]
    # f_out(matrix_a)
    # print("=" * 10)
    # f_out(matrix_b)
    set_matrix(matrix_a, "A")
    set_matrix(matrix_b, "B")

    # f_out(matrix_a)
    # print("=" * 10)
    # f_out(matrix_b)

    matrix_c = add(matrix_a, matrix_b)
    output(matrix_c)

