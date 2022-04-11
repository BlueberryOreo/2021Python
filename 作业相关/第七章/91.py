def fibonacci(target, n=1, n1=0, n2=1):
    if target == -1:
        return 0
    if target == 0:
        return 1
    if n == target:
        return n1 + n2
    else:
        n3 = n1 + n2
        result = fibonacci(target, n=n+1, n1=n2, n2=n3)
    return result


if __name__ == "__main__":
    # for i in range(1, 100):
    #     print(i, fibonacci(i - 2))
    n = int(input())
    print(fibonacci(n - 1))
