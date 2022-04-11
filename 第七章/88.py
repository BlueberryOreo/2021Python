def factor_sum(n: int):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


if __name__ == "__main__":
    n = int(input())
    print(factor_sum(n))
