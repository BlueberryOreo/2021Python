def reverse(num: int):
    ret = 0
    length = 0
    temp = num
    while temp > 0:
        temp //= 10
        length += 1

    while num > 0:
        ret += num % 10 * 10 ** (length - 1)
        num //= 10
        length -= 1
    return ret


if __name__ == "__main__":
    a = int(input())
    print(reverse(a))
