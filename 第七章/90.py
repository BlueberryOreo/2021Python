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


def is_prime(n: int):
    flag = True
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag


def is_r_prime(n: int):
    if is_prime(n) and is_prime(reverse(n)) and reverse(n) != n:
        # print(n, reverse(n))
        return True
    else:
        return False


if __name__ == "__main__":
    c = 0
    count = 0
    i = 2
    while True:
        if is_r_prime(i):
            print("{:>5}".format(i), end="")
            count += 1
            c += 1
            if c == 8:
                print()
                c = 0
            if count == 30:
                break
        i += 1
